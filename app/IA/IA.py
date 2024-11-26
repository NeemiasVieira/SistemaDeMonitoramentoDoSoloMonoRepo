import numpy as np
import tensorflow as tf
from keras.preprocessing import image

LABELS_DETECTION = ["Sem planta", "Com planta"]
LABELS_HEALTH = [
    "A planta não apresenta sinais de deficiência de saúde nesse registro",
    "A planta apresenta sinal de deficiência nesse registro"
]

DETECTION_MODEL_PATH = './app/IA/models/plant_detection_model.tflite'
HEALTH_MODEL_PATH = './app/IA/models/model.tflite'

def load_and_preprocess_image(image_path, target_size=(224, 224)):
    """
    Carrega e pré-processa uma imagem para entrada nos modelos.
    """
    img = image.load_img(image_path, target_size=target_size)
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0) 
    img_array = img_array.astype(np.float32)  
    return img_array

# Função para fazer predições usando um modelo TFLite
def predict_with_tflite_model(model_path, image):
    """
    Realiza predição em uma imagem usando um modelo TFLite.
    """

    interpreter = tf.lite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()

    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], image)
    interpreter.invoke()
    prediction = interpreter.get_tensor(output_details[0]['index'])
    return prediction

def classify_image_with_pipeline(image_path):
    """
    Processa a imagem com dois modelos: detecção de plantas e classificação de saúde.
    """
    confidence_threshold = 0.7

    image = load_and_preprocess_image(image_path)

    detection_prediction = predict_with_tflite_model(DETECTION_MODEL_PATH, image)
    detection_label = np.argmax(detection_prediction)
    max_confidence_detection = np.max(detection_prediction)

    print(f"Detecção (Planta): {detection_prediction}")
    print(f"Confiança (Detecção): {max_confidence_detection}")

    if detection_label == 0 or max_confidence_detection < confidence_threshold:
        return "Não foi possível identificar uma planta na imagem fornecida"

    health_prediction = predict_with_tflite_model(HEALTH_MODEL_PATH, image)
    health_label = np.argmax(health_prediction)
    max_confidence_health = np.max(health_prediction)

    print(f"Classificação (Saúde): {health_prediction}")
    print(f"Confiança (Saúde): {max_confidence_health}")

    return LABELS_HEALTH[health_label]

def processarImagemComIA():
    """
    Processa a imagem usando dois modelos TFLite.
    """
    try:
        image_path = './app/IA/uploads/imagem.jpg'
        predicted_class = classify_image_with_pipeline(image_path)
        return predicted_class
    except Exception as e:
        return f'Erro ao processar imagem: {e}'

if __name__ == "__main__":
    result = processarImagemComIA()
    print(result)
