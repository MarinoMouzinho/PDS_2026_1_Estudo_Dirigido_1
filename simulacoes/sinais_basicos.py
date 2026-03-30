import numpy as np
import matplotlib.pyplot as plt
import os

def executar():

    n = np.arange(-20, 21)

    impulso = np.zeros_like(n)
    impulso[n == 0] = 1

    degrau = np.where(n >= 0, 1, 0)

    exponencial = 0.9 ** n

    plt.stem(n, impulso)
    plt.title("Impulso Unitário")
    plt.savefig("resultados/impulso.png")
    plt.clf()

    plt.stem(n, degrau)
    plt.title("Degrau Unitário")
    plt.savefig("resultados/degrau.png")
    plt.clf()

    plt.stem(n, exponencial)
    plt.title("Exponencial Discreta")
    plt.savefig("resultados/exponencial.png")
    plt.clf()