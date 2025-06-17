import serial
import time

porta_serial = serial.Serial('COM6', 9600, timeout=1)
time.sleep(2)

with open("dados_arduino.txt", "w") as arquivo:
    try:
        while True:
            if porta_serial.in_waiting > 0:
                linha = porta_serial.readline().decode('utf-8').strip()
                if linha:
                    arquivo.write(linha + "\n")
                    print(f"Valor salvo: {linha}")
    except KeyboardInterrupt:
        print("Dados salvos em 'dados_arduino.txt'")
        porta_serial.close()
