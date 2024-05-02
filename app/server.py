import RPi.GPIO as GPIO
import time
import schedule
import time
from sensor_lux import ler_sensor_lux
from utils.indicador_led import indica_envio_requisicao, ligar_led, desligar_led

# Código principal em looping (exemplo de uso)
if __name__ == '__main__':
    try:
        #Inicia o programa com o estado do led ativo (também pode ser colocado como última etapa para desmonstrar que todos os passos iniciais funcionaram bem)
        ligar_led()

        # Agenda a execução da função `indica_envio_requisicao` diariamente às 10h da manhã
        schedule.every().day.at("10:00").do(indica_envio_requisicao)

        # Agenda a execução da função `indica_envio_requisicao` a cada 5 minutos
        schedule.every(5).seconds.do(indica_envio_requisicao)

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
        
