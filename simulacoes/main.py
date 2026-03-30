import os

from sinais_basicos import executar as sinais_basicos
from operacoes_sinais import executar as operacoes
from energia_potencia import executar as energia
from classificacao_sistemas import executar as sistemas
from sensor_termico import executar as sensor

os.makedirs("resultados", exist_ok=True)

print("Executando sinais básicos...")
sinais_basicos()

print("Executando operações...")
operacoes()

print("Calculando energia e potência...")
energia()

print("Classificando sistemas...")
sistemas()

print("Simulando sensor térmico...")
sensor()

print("Tudo finalizado! Veja a pasta /resultados")