
---

# 🎯 Projeto DASA - Otimização de Pipeline de Visão Computacional (Programação Dinâmica)

Este módulo implementa uma solução de **Programação Dinâmica (PD)** para otimizar o tempo de processamento das análises macroscópicas em equipamentos de **Visão Computacional (VC)**.
O objetivo é encontrar o **agrupamento ótimo das etapas sequenciais da pipeline** para minimizar o custo total de interligação (tempo/recursos).

---

## 💡 Modelagem do Problema

O problema é modelado como uma variação do **Multiplicação em Cadeia de Matrizes (Chain Matrix Multiplication)**, onde o custo de interligação entre dois módulos é baseado na complexidade de **I/O** de suas extremidades.

| Componente                  | Conceito Aplicado                                                                                              |
| --------------------------- | -------------------------------------------------------------------------------------------------------------- |
| **Estados ($\mathbf{S}$)**  | $\text{DP}[i][j]$: Custo mínimo do módulo de processamento da etapa $i$ até a etapa $j$.                       |
| **Decisões ($\mathbf{D}$)** | Escolha do ponto de divisão $k$ ótimo, que resulta no custo mínimo para o módulo $[i, j]$.                     |
| **Função de Transição**     | $\text{DP}[i][j] = \min_{i \leq k < j} { \text{DP}[i][k] + \text{DP}[k+1][j] + \text{Custo de Interligação} }$ |
| **Custo de Interligação**   | Simulado por $P_{i-1} \times P_{k} \times P_{j}$, onde $P$ é a complexidade de I/O dos dados.                  |

---

## 🛠️ Implementação e Algoritmos

A solução foi desenvolvida em **Python** para garantir coerência e eficiência entre diferentes abordagens de **Programação Dinâmica**.

### 1. Algoritmos de PD

| Abordagem                               | Característica                                                                                                                                 | Complexidade |
| --------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- | ------------ |
| **Recursiva com Memoização (Top-Down)** | Utiliza um cache (tabela/dicionário) para armazenar os resultados dos subproblemas já calculados.                                              | $O(n^3)$     |
| **Iterativa (Bottom-Up)**               | Constrói a tabela de soluções (DP) de forma progressiva, partindo dos módulos menores (comprimento 2) até o módulo completo (comprimento $N$). | $O(n^3)$     |

---

### 2. Funcionalidade de Rastreamento (Split Table)

Para ir além do custo mínimo (um número), foi implementada uma funcionalidade crucial: o **rastreamento da solução ótima**.

* **Matriz Auxiliar `SPLIT`**
  É preenchida durante a execução **Bottom-Up** e armazena o ponto de quebra $k$ que levou ao custo mínimo para cada subproblema $\text{DP}[i][j]$.

* **Função de Reconstrução**
  Utiliza recursão para ler a matriz `SPLIT` e reconstruir a expressão de agrupamento ótima (parentização), fornecendo a recomendação prática de como o software deve agrupar as etapas de análise.

---

## 🚀 Como Executar

O projeto é executado através de uma **interface de menu no terminal**.

### 1. Clone o repositório:

```bash
git clone https://github.com/guilhermearaujodec/Sprint-4---Dynamic-Programming.git
cd Sprint-4---Dynamic-Programming
```

### 2. Execute o script Python:

```bash
python app.py
```

### 3. Interface do Usuário

* **Opção 1:** Permite ao usuário definir as complexidades de I/O da pipeline (`P0`, `P1`, `P2`...).
* **Opção 2:** Executa e compara as versões de PD, exibindo o **Custo Mínimo** e o **Agrupamento Ótimo**.

---

## 📈 Exemplo de Resultado

A otimização transforma uma lista de complexidades em uma estrutura de agrupamento que define a ordem de execução do equipamento.

| Entrada (Complexidades P)            | Resultado (Custo Mínimo) | Agrupamento Ótimo                                 |
| ------------------------------------ | ------------------------ | ------------------------------------------------- |
| `[30, 35, 15, 5, 10, 20]` (5 etapas) | 15,100                   | `((Etapa 1 (Etapa 2 Etapa 3)) (Etapa 4 Etapa 5))` |

---

## 🎓 Conclusão

A aplicação da **Programação Dinâmica** resolve o problema de otimização de forma eficiente, garantindo a complexidade de $O(N^3)$.
A inclusão da **matriz de rastreamento** transforma a solução teórica em uma **recomendação acionável para a engenharia de software da pipeline de Visão Computacional**, promovendo o uso eficiente dos recursos de hardware.

---



## 👨‍💻 Autores

<div align="center">

**Augusto Mendonça** — RM: `558371`  
**Gabriel Vasquez** — RM: `557056`  
**Guilherme Araujo** — RM: `558926`  
**Gustavo Oliveira** — RM: `559163`

</div>



---
