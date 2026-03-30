import numpy as np
import matplotlib.pyplot as plt

def executar():
    n = np.arange(-20, 21)
    x = np.sin(0.2 * np.pi * n)

    # deslocamento
    x_deslocado = np.sin(0.2 * np.pi * (n - 5))

    plt.stem(n, x, label="Original")
    plt.stem(n, x_deslocado, linefmt='r-', markerfmt='ro', label="Deslocado")
    plt.legend()
    plt.title("Deslocamento")
    plt.savefig("resultados/deslocamento.png")
    plt.clf()

    # inversão
    x_inv = np.sin(0.2 * np.pi * (-n))

    plt.stem(n, x, label="Original")
    plt.stem(n, x_inv, linefmt='r-', markerfmt='ro', label="Invertido")
    plt.legend()
    plt.title("Inversão")
    plt.savefig("resultados/inversao.png")
    plt.clf()