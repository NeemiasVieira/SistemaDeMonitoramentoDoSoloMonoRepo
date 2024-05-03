from picamera import PiCamera
import time
import os

# Inicializa a câmera
camera = PiCamera()

# Define o diretório de saída para salvar as imagens
diretorio = "../image"  # Substitua pelo caminho do diretório desejado

# Função para capturar uma foto
def capturar_foto():

    # Define o nome do arquivo com base no timestamp
    nome_arquivo = f"image.jpg"
    
    # Cria o caminho completo para o arquivo
    caminho_arquivo = os.path.join(diretorio, nome_arquivo)
    
    # Captura a foto e salva no diretório especificado
    camera.capture(caminho_arquivo)

