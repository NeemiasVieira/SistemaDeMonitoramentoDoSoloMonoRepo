import time
import serial

#Configurações do TTN:

dev_eui = '0012F80000001E5E'
app_eui = '0101010101010011'
app_key = '4607345DD2A3A1591E00CD162A1CB991'

#Configuração da porta serial
serial_port = '/dev/ttyAMA0'

#Função para enviar um comando para o módulo
def send_command(command):
    ser = serial.Serial(serial_port, baudrate = 9600, timeout=2)
    ser.write(command.encode() + b'\r\n')
    time.sleep(2)
    response = ser.read_all()
    print('Resposta: ', response.decode())
    ser.close()
                        
def join_ttn():
    #send_command('AT+DEV=' + dev_eui)
    #send_command('AT+APPEUI=' + app_eui)
    #send_command('AT+APPKEY=' + app_key)
    send_command('AT+JOIN')
    #send_command('AT')
    

#Função para enviar mensagens:
def send_message(message):
    #Configurando a porta serial:
    ser = serial.Serial(serial_port, baudrate = 9600, timeout=2)
    #Envia o comando de envio de mensagem
    ser.write(b'AT+SEND=1:' + bytes(message, 'utf-8') + b'\r\n')
    
    #Aguarda resposta
    time.sleep(2)
    #Lê a resposta
    response = ser.read_all()
    print('Resposta: ', response.decode())
    #Fecha a porta serial
    ser.close()

join_ttn()

while True:
    for c in range (1, 16):
        send_message(f'{str(c)}')
        time.sleep(20)
    for c in range (14, 0, -1):
        send_message(f'{str(c)}')
        time.sleep(20)
        
    
