import RPi.GPIO as GPIO
import time
import schedule
from services.sensor_lux import ler_sensor_lux
from services.indicador_led import indica_envio_requisicao, ligar_led, desligar_led, piscar_led
from services.api import uploadImagem, enviarRegistro, confirmarSolicitacao, verificarSolicitacao
from services.sensor_npk import ler_sensor_NPK
from services.camera import capturar_foto
from services.logger import logger

idPlanta = '652955aa670b516ea2a104d0'

def executar_leituras():
    logger.info("Executando rotina de leituras...")
    capturar_foto()
    imagem, diagnostico = uploadImagem('/home/tcc/Desktop/SensorMonitoramento/app/image/image.jpg')
    nitrogenio, fosforo, potassio, umidade, temperatura, pH = ler_sensor_NPK()
    luz = ler_sensor_lux()
    indica_envio_requisicao()
    resposta = enviarRegistro(idPlanta, nitrogenio, fosforo, potassio, umidade, temperatura, pH, luz, imagem, diagnostico)
    return resposta.json()

def verificarPendencias():
    logger.info("Executando rotina de verificação de pendências...")
    indica_envio_requisicao()
    verificacao = verificarSolicitacao(idPlanta)
    logger.debug(f"Status da verificação: ${verificacao}")

    if (verificacao == "aguardando"):
        resposta = executar_leituras()
        
        if(resposta is not None):
            indica_envio_requisicao()
            respostaConfirmacao = confirmarSolicitacao(idPlanta)
            logger.debug(f"Resposta da confirmação: ${respostaConfirmacao}")
    
if __name__ == '__main__':
    logger.info("Servidor iniciado com sucesso 🚀")
    try:
        schedule.every().day.at("10:00").do(verificarPendencias)

        schedule.every(5).seconds.do(verificarPendencias)

        while True:
            schedule.run_pending()
            time.sleep(1)  
        
    except KeyboardInterrupt:
        logger.debug("Servidor finalizado com sucesso ❌")
        desligar_led()

    except Exception as e:
        # Captura qualquer exceção
        logger.critical(f"Ocorreu um com o servidor: {e}")
        desligar_led()
        
    finally:
        piscar_led(3, 2)
        GPIO.cleanup()
        
