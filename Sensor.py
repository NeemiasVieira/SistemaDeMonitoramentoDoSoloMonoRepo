import minimalmodbus
import requests
import json

url = 'https://sms-api-git-main-neemiasvieira.vercel.app/registros'

# Configuração do objeto Modbus
instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
instrument.serial.baudrate = 4800  # Taxa de transmissão padrão do sensor (datasheet)
instrument.serial.timeout = 1  # Tempo limite para leitura

try:
    # Leitura dos registros
    umidade = instrument.read_register(0, functioncode=4, signed=True) * 0.1
    umidade = round(umidade, 1)
    temperatura = instrument.read_register(1, functioncode=4, signed=True) * 0.1
    temperatura = round(temperatura, 1)
    pH = instrument.read_register(3, functioncode=3, signed=True) * 0.1
    nitrogênio = (instrument.read_register(4, functioncode=3, signed=True) * 0.01) + 0.0
    pH = round(pH,1)
    fósforo = (instrument.read_register(5, functioncode=3, signed=True) * 0.01) + 0.0
    potássio = (instrument.read_register(6, functioncode=3, signed=True) * 0.01) + 0.0

    # Envio dos resultados para a API
#     data = {
#             "idPlanta": "652955aa670b516ea2a104d0",
#             "nitrogenio": str(nitrogênio),
#             "fosforo": str(fósforo),
#             "potassio": str(potássio),
#             "umidade": str(umidade),
#             "temperatura": str(temperatura),
#             "pH": str(pH)
#                 }
                
    # Enviar a requisição POST com o JSON no corpo
#     response = requests.post(url, json=data)

    # Verificar a resposta
 #   if response.status_code == 201:
  #      print("Requisição bem-sucedida!")
   #     print("Resposta:")
     #   print(response.text)
   # else:
    #    print("Falha na requisição, Código do erro:", response.status_code)
     #   print("Resposta:")
      #  print(response.text)

    # Imprime os resultados
    print("Umidade: {}%RH".format(umidade))
    print("Temperatura: {}°C".format(temperatura))
    print("pH: {}".format(pH))
    print("Nitrogênio(N): {}mg/kg".format(nitrogênio))
    print("Fósforo(P): {}mg/kg".format(fósforo))
    print("Potássio(K): {}mg/kg".format(potássio))

    # Definir o Slave ID
    novo_slave_id = 2
    instrument.write_register(40081, novo_slave_id, functioncode=6)

    # Consulta ao Slave ID
    consulta_slave_id = instrument.read_register(41257, functioncode=3)
    print("Slave ID atual: {}".format(consulta_slave_id))

except IOError as e:
    print("Erro de E/S:", str(e))
except ValueError as e:
    print("Erro de Valor:", str(e))
except minimalmodbus.NoResponseError:
    print("Não houve resposta do dispositivo Modbus.")
except minimalmodbus.InvalidResponseError:
    print("Resposta inválida do dispositivo Modbus.")
except minimalmodbus.CannotWriteToInstrument as e:
    print("Não foi possível escrever no dispositivo Modbus:", str(e))
except minimalmodbus.SerialException as e:
    print("Erro na comunicação serial:", str(e))
except Exception as e:
    print("Erro desconhecido:", str(e))
