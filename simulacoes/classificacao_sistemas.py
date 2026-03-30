import numpy as np
import matplotlib.pyplot as plt

def executar():
    n = np.arange(-20, 21)
    x = np.sin(0.2 * np.pi * n)

    # sistema com memória
    y_mem = np.zeros_like(x)
    for i in range(1, len(x)):
        y_mem[i] = x[i] + x[i-1]

    plt.stem(n, y_mem)
    plt.title("Sistema com Memória")
    plt.savefig("../resultados/sistema_memoria.png")
    plt.clf()

    # sistema não causal
    y_nc = np.roll(x, -1)

    plt.stem(n, y_nc)
    plt.title("Sistema Não Causal")
    plt.savefig("../resultados/sistema_nao_causal.png")
    plt.clf()