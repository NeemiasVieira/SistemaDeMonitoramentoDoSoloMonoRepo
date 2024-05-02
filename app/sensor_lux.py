import smbus
import time

# Define o endereço do sensor BH1750
BH1750_ADDR = 0x23

# Comando para configurar o sensor no modo de medição de alta resolução contínuo
BH1750_CONTINUOUS_HIGH_RES_MODE = 0x10

# Inicializa o barramento I2C
bus = smbus.SMBus(1)  # 1 para Raspberry Pi 3, 0 para Raspberry Pi 1

def setup():
    # Configura o sensor BH1750 no modo de medição de alta resolução contínuo
    bus.write_byte(BH1750_ADDR, BH1750_CONTINUOUS_HIGH_RES_MODE)
    time.sleep(0.2)  # Espera para o sensor se configurar

def read_light_level():
    # Lê os dados do sensor (2 bytes)
    data = bus.read_i2c_block_data(BH1750_ADDR, 0x00, 2)
    # Calcula o nível de luz em lux
    light_level = ((data[0] << 8) + data[1]) / 1.2
    return light_level

def main():
    print("BH1750 Test begin")
    try:
        while True:
            setup()
            lux = read_light_level()
            print("Light: {} lx".format(lux)) #Light: 295.83333333333337 lx
            time.sleep(1)
    except KeyboardInterrupt:
        pass

if __name__ == "__main__":
    main()