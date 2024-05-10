import minimalmodbus

def ler_sensor_NPK():

    # Configuração do objeto Modbus
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
    instrument.serial.baudrate = 4800  # Taxa de transmissão padrão do sensor (datasheet)
    instrument.serial.timeout = 1  # Tempo limite para leitura

    try:
        # Leitura dos registros
        nitrogênio = (instrument.read_register(4, functioncode=3, signed=True) * 0.01) + 0.0
        fósforo = (instrument.read_register(5, functioncode=3, signed=True) * 0.01) + 0.0
        potássio = (instrument.read_register(6, functioncode=3, signed=True) * 0.01) + 0.0

        umidade = instrument.read_register(0, functioncode=4, signed=True) * 0.1
        umidade = round(umidade, 1)

        temperatura = instrument.read_register(1, functioncode=4, signed=True) * 0.1
        temperatura = round(temperatura, 1)
        
        pH = instrument.read_register(3, functioncode=3, signed=True) * 0.1
        pH = round(pH,1)

        # Definir o Slave ID
        novo_slave_id = 2
        instrument.write_register(40081, novo_slave_id, functioncode=6)

        # Consulta ao Slave ID
        consulta_slave_id = instrument.read_register(41257, functioncode=3)
        print("Slave ID atual: {}".format(consulta_slave_id))

        return {
            "nitrogenio": str(nitrogênio),
            "fosforo": str(fósforo),
            "potassio": str(potássio),
            "umidade": str(umidade),
            "temperatura": str(temperatura),
            "pH": str(pH)
        }

    except IOError as e:
        print("Erro de E/S do sensor NPK:", str(e))
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

#Teste do sensor
#resposta = ler_sensor_NPK()
#print(resposta)