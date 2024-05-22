import cv2
import os
import time

def capturar_foto():
    diretorio_pai = os.path.dirname(os.getcwd())
    diretorio_image = os.path.join(diretorio_pai, "app" ,"image")

    if not os.path.exists(diretorio_image):
        os.makedirs(diretorio_image)
        print(f"Diretório {diretorio_image} criado.")

    webcam = cv2.VideoCapture(0)

    # Verifica se a webcam foi aberta corretamente
    if not webcam.isOpened():
        print("Erro: Não foi possível abrir a webcam.")
        return False

    # Aumenta o tempo de espera para 2 segundos
    time.sleep(2)

    # Captura e descarta alguns frames iniciais
    for i in range(5):
        webcam.read()

    retorno, imagem = webcam.read()

    if not retorno:
        print("Erro ao capturar a imagem.")
        webcam.release()
        return False

    nome_arquivo = "image.jpg"
    caminho_arquivo = os.path.join(diretorio_image, nome_arquivo)

    if cv2.imwrite(caminho_arquivo, imagem):
        print(f"Imagem salva com sucesso!")
    else:
        print("Erro ao salvar a imagem.")
        webcam.release()
        return False

    webcam.release()
    return True

foto_capturada = capturar_foto()

if foto_capturada:
    print("Foto capturada!")
else:
    print("Não foi possível capturar a foto.")
