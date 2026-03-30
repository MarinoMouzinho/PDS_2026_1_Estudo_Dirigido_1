# Resumo Teórico
## Modelagem de Sinais e Sistemas Discretos

**Curso:** Engenharia da Computação
**Discente:** Marino Paulino Mouzinho da Silva

---

## 1 Sinais Contínuos e Discretos 

Segundo Oppenheim e Schafer, um sinal é algo que transmite informação, seja do estado atual ou do comportamento de um sistema ao longo do tempo, podendo representar fenômenos físicos que variam continuamente ou de forma discreta. Matematicamente, sinais são representados como funções de uma ou mais variáveis independentes, sendo mais comum a variável tempo. Um sinal contínuo no tempo é descrito por uma função do tipo $x(t)$, onde $t∈R$, enquanto um sinal discreto é representado por uma sequência $x[n]$, onde $n∈Z$.

A obtenção de sinais discretos a partir de sinais contínuos ocorre por meio do processo de amostragem, no qual o sinal é avaliado em instantes discretos de tempo, tipicamente definidos por um período de amostragem $T_s$. Assim, um sinal discreto pode ser descrito como $x[n]=x(nT_s)$.

Do ponto de vista físico, os sinais discretos representam as medições reais obtidas por sensores. Por exemplo, um sensor de temperatura realiza leituras periódicas, gerando uma sequência numérica que representa sua evolução térmica ao longo do tempo. Da mesma forma, sensores de vibração em máquinas rotativas produzem sinais discretos que descrevem oscilações mecânicas.

---

## 2 Sequências Elementares

As sequências elementares são fundamentais na modelagem de sinais discretos, sendo amplamente utilizadas para análise e construção de sinais mais complexos. Entre as principais sequências destacam-se: o __impulso unitário__, o __degrau unitário__ e as __exponenciais__.

### 2.1 Impulso Unitário

O impulso unitário é definido como uma sequência que assume valor 1 quando n = 0 e 0 em todos os outros instantes. Ele é representado pela seguinte notação:
$$δ[n]$$
Essa sequência permite representar qualquer sinal discreto como uma combinação de impulsos deslocados, ou seja, o impulso pode atuar para decomposição de sinais. Matematicamente, expressa como:
$$x[n]=∑_{k=−∞}^∞x[k]δ[n−k]$$

### 2.2 Degrau Unitário

O degrau unitário, representado por $u[n]$, é definido como sendo 0 para valores negativos e 1 para valores positivos ou zero. Esse tipo de sinal é utilizado para modelar fenômenos que iniciam em um determinado instante, como o acionamento de um sistema ou o início de uma medição em sensores.

### 2.3 Exponenciais

As sequências exponenciais, da forma $x[n]=A⋅a^n$, também desempenham papel fundamental, podendo representar crescimento ou decaimento de sinais ao longo do tempo. Quando $∣a∣<1$, o sinal decai, sendo útil na modelagem de fenômenos como a perda de energia em sistemas físicos. Quando $∣a∣>1$, o sinal cresce, podendo representar instabilidades.

---

## 3 Operações com Sinais

As operações com sinais permitem modificar suas características temporais e de amplitude.

### 3.1 Deslocamento

O deslocamento temporal consiste em atrasar ou adiantar um sinal no tempo. Matematicamente, um atraso de $n_0$ amostras é representado por 
$x[n−n_0]$, enquanto um avanço é representado por $x[n+n_0]$. Essa operação é essencial na modelagem de sistemas que apresentam atraso,podendo representar o tempo necessário para que um sensor detecte uma mudança no ambiente, como o atraso na resposta de um sensor de temperatura ao aquecimento de um ambiente.

### 3.2 Inversão

A inversão temporal é representada por:
$$x[−n]$$
Ela consiste em refletir o sinal em torno do eixo vertical e está presente em análises matemáticas e em algumas aplicações de processamento, como correlação de sinais. A inversão não representa diretamente um fenômeno real, mas auxilia na análise de sistemas e na comparação entre sinais medidos e referências.

### 3.3 Escalonamento

O escalonamento de amplitude consiste em multiplicar o sinal por uma constante $Ax[n]$. Essa operação altera a intensidade do sinal sem modificar sua estrutura temporal. Isso pode representar amplificação ou atenuação de sinais provenientes de sensores, como o ganho aplicado a sinais elétricos em sistemas digitais ou embarcados.

---

## 4 Energia e Potência de Sinais

Sinais de energia são aqueles cuja energia total é finita, enquanto sinais de potência possuem energia infinita, mas potência média finita. Sinais de sensores podem ser classificados com base nessas características. Por exemplo, um sinal de vibração transitória, como um impacto em uma máquina, tende a ser um sinal de energia, enquanto sinais contínuos de operação, como a rotação constante de um eixo, são melhor descritos como sinais de potência.

A energia de um sinal discreto é definida como 

$$E=∑_{n=−∞}^∞∣x[n]∣^2$$

Enquanto a potência média é dada por 

$$P=\lim_{N→∞}​ \frac{1}{2N+1} \sum^N_{n=-N}|x[n]|²$$

A análise de energia e potência permite avaliar a intensidade do sinal e sua relevância para o processamento digital, sendo essencial para o projeto de algoritmos eficientes e robustos.

---

## 5 Classificação de Sistemas Discretos
Sistemas discretos são definidos como entidades que transformam um sinal de entrada $x[n]$ em um sinal de saída $y[n]$. A análise das propriedades estruturais desses sistemas é fundamental para garantir o correto processamento de sinais de sensores reais.

### 5.1 Memória

Um sistema possui memória quando sua saída depende de valores passados ou futuros da entrada. Caso contrário, é dito sem memória.

Como exemplo de sistema sem memória, pode-se considerar:
$$y[n]=2x[n]$$
No qual a saída em cada instante depende apenas do valor da entrada naquele mesmo instante. Já um exemplo de sistema com memória é dado por: 
$$y[n]=x[n]+x[n−1]$$
Onde a saída depende tanto do valor atual quanto do valor anterior da entrada.

### 5.2 Causalidade

Um sistema é causal se sua saída em um determinado instante depende apenas de valores presentes e passados da entrada. No contexto de sensores, a causalidade garante que o processamento do sinal ocorra de forma física e implementável.

Um exemplo de sistema causal é:

$$y[n]=x[n]+x[n−1]$$

Pois a saída depende apenas do presente e do passado. Em contrapartida, o sistema:

$$y[n]=x[n+1]$$

É não causal, pois depende de um valor futuro da entrada.


### 5.3 Variança no Tempo

Um sistema é invariante no tempo se seu comportamento não muda ao longo do tempo. Isso significa que um deslocamento na entrada resulta em um deslocamento equivalente na saída. Sistemas variantes no tempo podem apresentar comportamento imprevisível, o que pode comprometer o processamento de sinais.

Matematicamente, se um sistema satisfaz 

$$x[n]→y[n]$$

Então ele é __invariante no tempo__ se:

$$x[n−n_0]→y[n−n_0]$$

Como exemplo, o sistema 

$$y[n]=x[n]+1$$ 

É __invariante__ no tempo, pois um deslocamento na entrada resulta em um deslocamento equivalente na saída.

### 5.4 Invertibilidade

Um sistema é invertível se é possível recuperar a entrada a partir da saída. Essa propriedade é importante em aplicações onde se deseja reconstruir o sinal original após processamento, como em sistemas de comunicação ou aquisição de dados.

Como exemplo de sistema invertível, pode-se considerar 

$$y[n]=2x[n]$$

Cuja inversa é dada por:

$$x[n]=\frac{y[n]}{2}$$

Nesse caso, não há perda de informação no processo. Por outro lado, o sistema 

$$y[n]=x^2[n]$$ 

não é invertível, pois diferentes entradas podem gerar a mesma saída. Por exemplo, $x[n]=2$ e $x[n]=−2$ produzem a mesma saída $y[n]=4$, impossibilitando a recuperação do sinal original.

### 5.5 Estabilidade BIBO

A estabilidade BIBO (Bounded Input, Bounded Output) garante que um sistema produza saída limitada para qualquer entrada limitada. Isso significa que se existe um valor finito $M$ tal que $∣x[n]∣≤M$, então deve existir um valor finito $K$ tal que $∣y[n]∣≤K$. Essa propriedade garante que ruídos ou variações na entrada não causem comportamentos instáveis no sistema.

Um exemplo de sistema estável é 

$$y[n]=0.5x[n]$$

Pois qualquer entrada limitada resultará em uma saída também limitada. Já o sistema 

$$y[n]=n⋅x[n]$$ 

Pode ser instável, pois mesmo que a entrada seja limitada, o fator 
$n$ pode fazer com que a saída cresça indefinidamente.