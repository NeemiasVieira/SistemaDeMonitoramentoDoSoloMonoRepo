import RPi.GPIO as GPIO
import time
import schedule
from services.sensor_lux import ler_sensor_lux
from services.indicador_led import indica_envio_requisicao, ligar_led, desligar_led
from services.api import uploadImagem, enviarRegistro, confirmarSolicitacao, verificarSolicitacao
from services.sensor_npk import ler_sensor_NPK
from services.camera import capturar_foto

idPlanta = '652955aa670b516ea2a104d0'

def executar_leituras():
    capturar_foto()
    imagem, diagnostico = uploadImagem('image/image.jpg')
    nitrogenio, fosforo, potassio, umidade, temperatura, pH = ler_sensor_NPK().values()
    luz = ler_sensor_lux()
    luz = str(luz)
    indica_envio_requisicao()
    resposta = enviarRegistro(idPlanta, nitrogenio, fosforo, potassio, umidade, temperatura, pH, luz, imagem, diagnostico)
    return resposta

def verificarPendencias():
    indica_envio_requisicao()

    if (verificarSolicitacao(idPlanta) == "aguardando"):
        resposta = executar_leituras()
        
        if(resposta):
            indica_envio_requisicao()
            confirmarSolicitacao(idPlanta)
    

# Código principal em looping (exemplo de uso)
if __name__ == '__main__':
    try:
        #Inicia o programa com o estado do led ativo (também pode ser colocado como última etapa para desmonstrar que todos os passos iniciais funcionaram bem)
        ligar_led()

        # Agenda a execução da função `indica_envio_requisicao` diariamente às 10h da manhã
        schedule.every().day.at("10:00").do(executar_leituras)

        # Agenda a execução da função `indica_envio_requisicao` a cada 5 minutos
        schedule.every(5).seconds.do(verificarPendencias)

        # Mantém o programa em execução para que o agendador possa funcionar
        while True:
            schedule.run_pending()
            print(ler_sensor_lux())
            time.sleep(1)  # Verifica as tarefas pendentes a cada 1 segundo
        
    except KeyboardInterrupt:
        print("Usuário solicitou o desligamento do servidor")
        desligar_led()

    except Exception as e:
        # Captura qualquer exceção
        print(f"Ocorreu um com o servidor: {e}")
        desligar_led()
        
    finally:
        GPIO.cleanup()
        
