# Estudo Dirigido – Parte 1
## Modelagem de Sinais e Sistemas Discretos

**Curso:** Engenharia da Computação
**Discente:** Marino Paulino Mouzinho da Silva

---

## Descrição 

Este repositório apresenta o desenvolvimento da Parte 1 do Estudo Dirigido da disciplina de Processamento Digital de Sinais, cujo foco está na modelagem de sinais discretos e na análise de sistemas digitais.

O trabalho integra fundamentos teóricos, simulações computacionais e interpretação de resultados, com o objetivo de compreender como sinais provenientes de sensores reais podem ser representados matematicamente e processados de forma adequada em sistemas digitais.

---

## Como Executar o Projeto

Clone este repositório:

```bash
git clone <link-do-repositorio>
```

Acesse a pasta do projeto e execute o script de simulação:

```bash
python simulacoes/main.py
```

Os gráficos serão gerados automaticamente na pasta `/resultados`.

---

## Estrutura do Repositório

```
\teoria
   resumo.md

\simulacoes
   main.py
   sinais_basicos.py
   operacoes_sinais.py
   energia_potencia.py
   classificacao_sistema.py
   sensor_termico.py

\resultados  
   (gerados automaticamente)
   
README.md
```
---

## Fundamentação Teórica

A base teórica do trabalho está fundamentada nos conceitos de sinais contínuos e discretos, sequências elementares, operações com sinais, energia e potência, e classificação de sistemas discretos.

As propriedades estruturais dos sistemas, como causalidade, estabilidade, linearidade e memória, são fundamentais para garantir que o processamento dos sinais seja confiável e fisicamente realizável.

---

## Simulações Desenvolvidas

As simulações foram implementadas em Python de forma modular, com cada arquivo representando um conjunto específico de conceitos do processamento digital de sinais.

Os módulos desenvolvidos foram:

- sinais_basicos.py
Geração de sequências elementares: impulso unitário, degrau unitário e exponencial discreta.

- operacoes_sinais.py
Aplicação de operações fundamentais em sinais, como deslocamento e inversão temporal.

- energia_potencia.py
Cálculo da energia e da potência de sinais discretos.

- classificacao_sistema.py
Simulação de sistemas discretos com foco em propriedades como memória e causalidade.

- sensor_termico.py
Modelagem de um sensor térmico real, incluindo comportamento dinâmico e presença de ruído.

Todas as simulações são executadas de forma centralizada pelo arquivo main.py.

---

## Resultados e Análises

A geração de sinais básicos permitiu compreender a construção de sinais discretos a partir de sequências elementares, fundamentais para a modelagem matemática de fenômenos reais.

As operações de deslocamento e inversão evidenciaram como sinais podem ser manipulados no domínio do tempo, representando situações práticas como atraso de sensores e análise temporal de dados.

O cálculo da energia e da potência permitiu caracterizar a intensidade dos sinais, sendo relevante em aplicações como monitoramento de vibração, onde variações energéticas podem indicar falhas mecânicas.

Na análise de sistemas, foi possível observar o comportamento de sistemas com memória, que utilizam valores passados do sinal, característica essencial em filtros digitais. Também foi analisado um sistema não causal, evidenciando sua inviabilidade prática em sistemas reais.

A simulação do sensor térmico demonstrou como um fenômeno físico pode ser representado matematicamente, incluindo a presença de ruído, o que aproxima o modelo da realidade. Esse tipo de sinal é comum em aplicações industriais e sistemas embarcados.

---

## Conexão com o Problema Norteador

A representação matemática do comportamento temporal de um sensor real é realizada por meio de sinais discretos obtidos por amostragem. Cada valor da sequência representa uma medição realizada em um instante específico, permitindo descrever a evolução temporal de grandezas físicas.

Para garantir o correto processamento desses sinais, é necessário analisar propriedades estruturais dos sistemas, como causalidade, estabilidade e memória. Essas propriedades asseguram que o sistema seja implementável, confiável e capaz de produzir resultados consistentes.

Assim, o estudo demonstra que a modelagem matemática e a análise de sistemas são fundamentais para o desenvolvimento de soluções em processamento digital de sinais aplicadas a sensores reais.