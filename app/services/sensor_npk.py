import minimalmodbus
from services.logger import logger

def ler_sensor_NPK():

    # Configuração do objeto Modbus
    instrument = minimalmodbus.Instrument('/dev/ttyUSB0', 1)
    instrument.serial.baudrate = 4800  # Taxa de transmissão padrão do sensor (datasheet)
    instrument.serial.timeout = 1  # Tempo limite para leitura
    
    try:
        logger.info("Iniciando leitura do sensor NPK...")
        # Leitura dos registros
        nitrogênio = (instrument.read_register(4, functioncode=3, signed=True)) + 0.0
        fósforo = (instrument.read_register(5, functioncode=3, signed=True)) + 0.0
        potássio = (instrument.read_register(6, functioncode=3, signed=True)) + 0.0

        umidade = instrument.read_register(0, functioncode=4, signed=True) * 0.1
        umidade = round(umidade, 1)

        temperatura = instrument.read_register(1, functioncode=4, signed=True) * 0.1
        temperatura = round(temperatura, 1)
        
        pH = instrument.read_register(3, functioncode=3, signed=True) * 0.1
        pH = round(pH,1)

        return {
            "nitrogenio": str(nitrogênio),
            "fosforo": str(fósforo),
            "potassio": str(potássio),
            "umidade": str(umidade),
            "temperatura": str(temperatura),
            "pH": str(pH)
        }.values()

    except IOError as e:
        logger.error("Erro de E/S do sensor NPK:", str(e))
    except ValueError as e:
        logger.error("Erro de Valor:", str(e))
    except minimalmodbus.NoResponseError:
        logger.error("Não houve resposta do dispositivo Modbus.")
    except minimalmodbus.InvalidResponseError:
        logger.error("Resposta inválida do dispositivo Modbus.")
    except minimalmodbus.CannotWriteToInstrument as e:
        logger.error("Não foi possível escrever no dispositivo Modbus:", str(e))
    except minimalmodbus.SerialException as e:
        logger.error("Erro na comunicação serial:", str(e))
    except Exception as e:
        logger.error("Erro desconhecido:", str(e))


if __name__ == "__main__":
    resposta = ler_sensor_NPK()
    logger.debug(resposta)