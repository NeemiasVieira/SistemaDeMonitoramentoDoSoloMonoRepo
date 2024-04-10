from flask import jsonify, request
from app import app
from app.IA.IA import processarImagemComIA
from dotenv import load_dotenv
import requests
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")


@app.route('/upload', methods=['POST'])
def processarImagem():
    print(request.files)
    if 'image' not in request.files:
        return jsonify({'erro': 'Nenhuma imagem fornecida'}), 400

    image = request.files['image']
    upload_folder = './app/IA/uploads'
    image_path = os.path.join(upload_folder, 'imagem.jpg')
    image.save(image_path)
    
    resultado = processarImagemComIA()
    link = uploadImagem(image_path)

    return jsonify({'diagnostico': resultado, 'imagem': link}), 200

def uploadImagem(image_path):
    try:
        form_data = {'image': open(image_path, 'rb')}
        response = requests.post('https://api.imgur.com/3/image', files=form_data, headers={'Authorization': f'Client-ID {client_id}'}, verify=False)
        print(response.json())

        if response.status_code == 200:
            return response.json().get('data').get('link')
        else:
            return jsonify({'error': 'Erro no upload da imagem'}), 500
    except Exception as e:
        return jsonify({'error': f'Erro no upload da imagem: {e}'}), 500
