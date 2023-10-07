import minimalmodbus
import serial

ser = serial.Serial('/dev/ttyAMA0', baudrate=4800, timeout=1)


# Configuração do dispositivo Modbus
instrument = minimalmodbus.Instrument('/dev/ttyAMA0', 1)  # Porta serial e endereço do dispositivo
instrument.serial.baudrate = 4800  # Taxa de baud
instrument.serial.bytesize = 8  # Bits de dados
instrument.serial.parity = minimalmodbus.serial.PARITY_NONE  # Nenhuma paridade
instrument.serial.stopbits = 1  # 1 bit de parada

try:
    # Ler os valores da tabela Modbus
    humidity = instrument.read_register(1, 1) / 10.0  # Endereço 40002, Humidity
    temperature = instrument.read_register(0, 1) / 10.0  # Endereço 40001, Temperature
    conductivity = instrument.read_register(2, 1)  # Endereço 40003, Conductivity
    ph = instrument.read_register(3, 1) / 10.0  # Endereço 40004, pH
    salinity = instrument.read_register(7, 1)  # Endereço 40008, Salinity
    tds = instrument.read_register(8, 1)  # Endereço 40009, TDS

    # Imprimir os valores lidos
    print(f'Humidity: {humidity} %RH')
    print(f'Temperature: {temperature} ℃')
    print(f'Conductivity: {conductivity}')
    print(f'pH: {ph}')
    print(f'Salinity: {salinity}')
    print(f'TDS: {tds}')

except Exception as e:
    print(f'Erro: {e}')
