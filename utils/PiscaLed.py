import RPi.GPIO as GPIO
import time

LED_PIN = 18  #Substituir pela porta que o led foi conectado

GPIO.setmode(GPIO.BCM)  
GPIO.setup(LED_PIN, GPIO.OUT)
GPIO.output(LED_PIN, GPIO.LOW)  


def ligar_led():
    GPIO.output(LED_PIN, GPIO.HIGH)

def desligar_led():
    GPIO.output(LED_PIN, GPIO.LOW)

def piscar_led(vezes=2, intervalo=0.5):
    for _ in range(vezes):
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(intervalo)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(intervalo)

def indica_envio_requisicao():
    piscar_led(vezes=2, intervalo=0.5)

# Código principal (exemplo de uso)
if __name__ == '__main__':
    try:
        #Inicia o programa com o estado do led ativo (também pode ser colocado como última etapa para desmonstrar que todos os passos iniciais funcionaram bem)
        ligar_led()

        # Exemplo de uso: Piscar o LED duas vezes para indicar o envio de uma requisição
        indica_envio_requisicao()
        
        
    except KeyboardInterrupt:
        print("Servidor encontrou algum erro e encerrou o processo")
        desligar_led()

    finally:
        GPIO.cleanup()
