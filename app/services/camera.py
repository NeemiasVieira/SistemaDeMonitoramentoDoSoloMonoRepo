import cv2
import os
import time
from services.logger import logger

def capturar_foto():
    diretorio_pai = os.path.dirname(os.getcwd())
    diretorio_image = os.path.join(diretorio_pai, "SensorMonitoramento", "app" ,"image")

    if not os.path.exists(diretorio_image):
        os.makedirs(diretorio_image)
        logger.info(f"Diretório {diretorio_image} criado.")

    webcam = cv2.VideoCapture(0)

    # Verifica se a webcam foi aberta corretamente
    if not webcam.isOpened():
        logger.error("Erro: Não foi possível abrir a webcam.")
        return False

    # Aumenta o tempo de espera para 2 segundos
    time.sleep(2)

    # Captura e descarta alguns frames iniciais
    for i in range(5):
        webcam.read()

    logger.info("Capturando a imagem com a câmera...")
    retorno, imagem = webcam.read()

    if not retorno:
        logger.error("Erro ao capturar a imagem.")
        webcam.release()
        return False

    nome_arquivo = "image.jpg"
    caminho_arquivo = os.path.join(diretorio_image, nome_arquivo)

    if cv2.imwrite(caminho_arquivo, imagem):
        logger.debug(f"Imagem salva com sucesso!")
    else:
        logger.error("Erro ao salvar a imagem.")
        webcam.release()
        return False

    webcam.release()
    return True

if __name__ == "__main__":

    foto_capturada = capturar_foto()

    if foto_capturada:
        logger.debug("Foto capturada!")
    else:
        logger.error("Não foi possível capturar a foto.")
