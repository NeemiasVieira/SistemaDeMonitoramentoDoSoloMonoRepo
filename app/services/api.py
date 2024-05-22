import requests

email = ""
senha = ""

def verificarSolicitacao(idPlanta): 
    api_url = 'http://172.212.98.90:3333/graphql'
    token = getToken()
    query = '''
       query Query($idPlanta: String!) {
         getSolicitacaoRegistro(idPlanta: $idPlanta)
            } '''

    variables = { 'idPlanta': idPlanta }
    json_data = {'query': query,'variables': variables }
    headers = {'Content-Type': 'application/json','Authorization': token }

    return requests.post(api_url, json=json_data, headers=headers).json().get('data').get('getSolicitacaoRegistro')

def confirmarSolicitacao(idPlanta):
    api_url = 'http://172.212.98.90:3333/graphql'
    token = getToken()
    mutation = '''
       mutation Mutation($idPlanta: String!, $confirmado: Boolean) {
            updateSolicitacaoRegistro(idPlanta: $idPlanta, confirmado: $confirmado) {
                solicitacaoNovoRegistro
                    }
                        } '''

    variables = { 'idPlanta': idPlanta, 'confirmado': True }
    json_data = {'query': mutation,'variables': variables }
    headers = {'Content-Type': 'application/json','Authorization': token }

    return requests.post(api_url, json=json_data, headers=headers).json().get('data').get('updateSolicitacaoRegistro').get('solicitacaoNovoRegistro')

#Funcao que envia o registro
def enviarRegistro(idPlanta, nitrogenio, fosforo, potassio, umidade, temperatura, pH, luz, imagem = None, diagnostico = None):
    api_url = 'http://172.212.98.90:3333/graphql'
    token = getToken()
    mutation = '''
        mutation Mutation($idPlanta: String!, $nitrogenio: String!, $fosforo: String!, $potassio: String!, $umidade: String!, $temperatura: String!, $pH: String!, $lux: String!, $imagem: String, $diagnostico: String) {
            createRecord(idPlanta: $idPlanta, nitrogenio: $nitrogenio, fosforo: $fosforo, potassio: $potassio, umidade: $umidade, temperatura: $temperatura, pH: $pH, lux: $lux, imagem: $imagem, diagnostico: $diagnostico) {
                id idPlanta nitrogenio fosforo potassio umidade temperatura pH luz dataDeRegistro imagem diagnostico } } '''

    variables = { 'idPlanta': idPlanta,'nitrogenio': nitrogenio,'fosforo': fosforo,'potassio': potassio,'umidade': umidade,'temperatura': temperatura, 'pH': pH, 'lux': luz, 'imagem': imagem, 'diagnostico': diagnostico }
    json_data = {'query': mutation,'variables': variables }
    headers = {'Content-Type': 'application/json','Authorization': token }

    return requests.post(api_url, json=json_data, headers=headers).json()

#Funçao que retorna o token de acesso (login)
def getToken():
    api_url = 'http://172.212.98.90:3333/graphql'
    query = '''
        query Query($email: String!, $senha: String!) {
            getToken(email: $email, senha: $senha) {
                Authorization } } '''
    variablesQuery = { 'email': email, 'senha': senha }
    json_dataQuery = {'query': query,'variables': variablesQuery }
    headersQuery = {'Content-Type': 'application/json' }

    try:
        response = requests.post(api_url, json=json_dataQuery, headers=headersQuery)
        data = response.json()
        
        if 'errors' in data:
            raise ValueError({'erro': data['errors']})
        
        token = data['data']['getToken']['Authorization']
        return token
    except Exception as e:
        raise ValueError({'erro': str(e)})

#Funçao responsável por executar o upload e processamento da imagem
def uploadImagem(imagem_path):
    api_url = 'http://172.212.98.90:8080/upload'
    files = {'image': open(imagem_path, 'rb')}

    resposta = requests.post(api_url, files=files).json()
    diagnostico = resposta.get('diagnostico')
    imagem = resposta.get('imagem')

    return imagem, diagnostico


#Exemplo de uso
nitrogenio = '50'
fosforo = '150'
potassio = '300'
umidade = '50'
temperatura = '21'
pH = '7'
luz = '10000'

#Atençao, o caminho da imagem passado para uploadImagem deve ser relativo a funçao de uploadImagem
imagem, diagnostico = uploadImagem('image/image.jpg')
token = getToken()

#O registro pode ser enviado com ou sem imagem e diagnostico
resposta = enviarRegistro('652955aa670b516ea2a104d0', nitrogenio, fosforo, potassio, umidade, temperatura, pH, luz, imagem, diagnostico)
print(resposta)
