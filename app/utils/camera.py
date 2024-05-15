import cv2
import os
import time

def capturar_foto():

    diretorio_pai = os.path.dirname(os.getcwd())
    diretorio_image = os.path.join(diretorio_pai, "image")

    if not os.path.exists(diretorio_image):
        os.makedirs(diretorio_image)

    webcam = cv2.VideoCapture(0)

    time.sleep(1)

    retorno, imagem = webcam.read()

    if retorno:
        nome_arquivo = f"image.jpg"
        caminho_arquivo = os.path.join(diretorio_image, nome_arquivo)
        cv2.imwrite(caminho_arquivo, imagem)
        webcam.release()

        return True
    else:
        print("Erro ao capturar a imagem.")
        return False

foto_capturada = capturar_foto()

if foto_capturada:
    print("Foto capturada!")
else:
    print("Não foi possível capturar a foto.")
