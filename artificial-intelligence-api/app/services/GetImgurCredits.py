from flask import jsonify, request
from app import app
from dotenv import load_dotenv
import requests
import os

load_dotenv()

client_id = os.getenv("CLIENT_ID")

@app.route('/credits', methods=['GET'])
def getCredits():
  response = requests.get('https://api.imgur.com/3/credits', headers={'Authorization': f'Client-ID {client_id}'}, verify=False)
  return jsonify({"resposta": response.json()}), 200
 