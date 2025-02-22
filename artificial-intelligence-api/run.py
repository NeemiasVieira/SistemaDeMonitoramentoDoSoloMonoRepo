from app import app
from flask import Flask, request, jsonify
#executar export PYTHONDONTWRITEBYTECODE=1

@app.after_request
def add_cors_headers(response):
    response.headers["Access-Control-Allow-Origin"] = "*"
    response.headers["Access-Control-Allow-Headers"] = "Content-Type,Authorization"
    response.headers["Access-Control-Allow-Methods"] = "GET,POST,PUT,DELETE,OPTIONS"
    return response

if __name__ == '__main__':
    # Iniciando o aplicativo Flask
    app.run(debug=True, port=8080, host='0.0.0.0')
