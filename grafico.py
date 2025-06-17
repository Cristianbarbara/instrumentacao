import serial
import matplotlib.pyplot as plt
import numpy as np

# Configuração da porta serial
porta_serial = serial.Serial('COM6', 9600, timeout=2)
plt.ion()  # Modo interativo

# Listas para armazenar dados
angulos = []
valores = []

# Configuração do gráfico
fig, ax = plt.subplots()
ax.set_xlabel("Ângulo (graus)")
ax.set_ylabel("Valor do Sensor (A0)")
ax.set_title("Leitura do Sensor vs. Ângulo do Motor")
ax.grid(True)

try:
    while True:
        if porta_serial.in_waiting > 0:
            linha = porta_serial.readline().decode('utf-8').strip()
            
            if "," in linha:  # Dados válidos
                angulo, valor = linha.split(",")
                angulos.append(int(angulo))
                valores.append(int(valor))
                
                # Atualiza gráfico
                ax.clear()
                ax.plot(angulos, valores, 'bo-')
                ax.set_xlim(0, 360)
                plt.pause(0.01)
                
            elif "Fim do ciclo" in linha:
                print("Ciclo completo!")
                break

except KeyboardInterrupt:
    print("Leitura interrompida")

finally:
    porta_serial.close()
    plt.ioff()
    
    # Salva dados em CSV
    np.savetxt("dados_angulo_sensor.csv", np.column_stack((angulos, valores)), 
               delimiter=",", header="Ângulo,Valor", fmt="%d")
    
    # Gráfico final
    plt.figure(figsize=(10, 5))
    plt.plot(angulos, valores, 'r-')
    plt.xlabel("Ângulo (graus)")
    plt.ylabel("Valor do Sensor (A0)")
    plt.grid(True)
    plt.show()
