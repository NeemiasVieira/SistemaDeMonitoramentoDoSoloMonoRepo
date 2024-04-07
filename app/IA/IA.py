import os
import numpy as np
import tensorflow as tf
from keras.preprocessing import image

# Carregando o modelo salvo
model_path = './app/IA/model/model.keras'
model = tf.keras.models.load_model(model_path)

# Função para carregar e pré-processar uma imagem
def load_and_preprocess_image(image_path, target_size):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    return img_array

# Função para classificar a imagem
def classify_image(image_path, target_size=(160, 160)):
    # Carregando e pré-processando a imagem
    img = load_and_preprocess_image(image_path, target_size)
    
    # Fazendo a previsão usando o modelo carregado
    prediction = model.predict(img)
    
    # Convertendo a previsão em uma classe (saudável ou não saudável)
    class_names = ["Nao Saudável", "Saudável"]
    predicted_class = class_names[int(round(prediction[0][0]))]
    
    return predicted_class

def processarImagemComIA():
    try:
        image_path = './app/IA/uploads/imagem.jpg'
        predicted_class = classify_image(image_path)
        return predicted_class
    except Exception as e:
        return f'Erro ao processar imagem: {e}';
  