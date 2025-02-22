import RPi.GPIO as GPIO
import time
from services.logger import logger

LED_PIN = 18  #Substituir pela porta que o led foi conectado

def setup_led():
    GPIO.setmode(GPIO.BCM)  
    GPIO.setup(LED_PIN, GPIO.OUT)
    GPIO.output(LED_PIN, GPIO.LOW)  

def ligar_led():
    setup_led()
    GPIO.output(LED_PIN, GPIO.HIGH)

def desligar_led():
    setup_led()
    GPIO.output(LED_PIN, GPIO.LOW)

def piscar_led(vezes=2, intervalo=0.5):
    setup_led()
    for _ in range(vezes):
        GPIO.output(LED_PIN, GPIO.LOW)
        time.sleep(intervalo)
        GPIO.output(LED_PIN, GPIO.HIGH)
        time.sleep(intervalo)

def indica_envio_requisicao():
    logger.info("LED - Indicando envio da requisição")
    piscar_led(vezes=2, intervalo=0.2)


if __name__ == "__main__":
    i = 0
    while(c < 10):
        indica_envio_requisicao()
        time.sleep(5)
        c = c+1