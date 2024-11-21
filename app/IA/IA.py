import numpy as np
import os
import tensorflow as tf
from keras.preprocessing import image


LABELS = [
    "A planta não apresenta sinais de deficiência de saúde nesse registro",
    "A planta apresenta sinal de deficiência nesse registro"
]

# Função para carregar e pré-processar uma imagem
def load_and_preprocess_image(image_path, target_size=(224, 224)):
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Adiciona dimensão de batch
    img_array = img_array.astype(np.float32)  # Certifique-se de que os dados estão no tipo certo
    return img_array

# Função para classificar a imagem
def classify_image(image_path):
    confidence_threshold = 0.7
    model_path = './app/IA/models/model.tflite'

    # Carregar o modelo TFLite
    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    # Obter detalhes dos tensores de entrada e saída
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    # Carregar e pré-processar a imagem
    image = load_and_preprocess_image(image_path)

    # Fazer a inferência
    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])

    # Encontra a classe com maior probabilidade
    max_confidence = np.max(prediction)

    # Depuração para entender os valores previstos
    print(f"Prediction Probabilities: {prediction}")
    print(f"Max Confidence: {max_confidence}")

    # Verifica se a confiança está abaixo do limiar
    if max_confidence < confidence_threshold:
        return "Não foi possível identificar uma planta na imagem fornecida"
    
    return LABELS[np.argmax(prediction)]

def processarImagemComIA():
    try:
        image_path = './app/IA/uploads/imagem.jpg'
        predicted_class = classify_image(image_path)
        return predicted_class
    except Exception as e:
        return f'Erro ao processar imagem: {e}';
  