import numpy as np

def executar():
    n = np.arange(-50, 51)
    x = np.sin(0.1 * np.pi * n)

    energia = np.sum(np.abs(x)**2)

    potencia = np.mean(np.abs(x)**2)

    print("Energia do sinal:", energia)
    print("Potência do sinal:", potencia)