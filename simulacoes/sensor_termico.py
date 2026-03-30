import numpy as np
import matplotlib.pyplot as plt

def executar():
    n = np.arange(0, 50)

    # simulação de aquecimento
    temperatura = 25 + 10 * (1 - np.exp(-0.1 * n))

    # ruído
    ruido = np.random.normal(0, 0.5, size=len(n))

    sinal_sensor = temperatura + ruido

    plt.plot(n, temperatura, label="Temperatura real")
    plt.plot(n, sinal_sensor, label="Sensor (com ruído)")
    plt.legend()
    plt.title("Sensor Térmico")
    plt.savefig("resultados/sensor_termico.png")
    plt.clf()