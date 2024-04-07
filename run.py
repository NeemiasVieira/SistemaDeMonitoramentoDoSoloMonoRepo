from app import app
#executar export PYTHONDONTWRITEBYTECODE=1
if __name__ == '__main__':
    # Iniciando o aplicativo Flask
    app.run(debug=True, port=8080, host='0.0.0.0')
