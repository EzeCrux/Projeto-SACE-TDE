📊 Sistema de Análise Combinatória e Estatística
🎯 Objetivo do Programa
Este sistema foi desenvolvido como parte do Trabalho Dirigido de Estudos (TDE) da disciplina de Matemática Computacional. O objetivo é aplicar conceitos de combinatória, probabilidade, recursividade e estatística, resolvendo problemas matemáticos por meio de programação, sem o uso de bibliotecas prontas.

🛠 Tecnologias Utilizadas
Linguagem: Python

Restrições: Sem uso de bibliotecas como math, numpy, statistics

Implementação: Todas as funções matemáticas foram escritas manualmente, com lógica própria.

📌 Funções Implementadas
🔁 Permutação
python
Copiar
Editar
def permutacao(n):
    return fatorial(n)
Calcula o total de maneiras de permutar n elementos.
Fórmula: P(n) = n!

🔀 Combinação
python
Copiar
Editar
def combinacao(n, p):
    return fatorial(n) // (fatorial(p) * fatorial(n - p))
Calcula quantos subconjuntos com p elementos podem ser formados a partir de n.
Fórmula: C(n, p) = n! / (p!(n-p)!)

🕊 Princípio das Casas de Pombo
python
Copiar
Editar
def principio_das_casas_de_pombo(pombos, casas):
    return pombos > casas
Verifica se haverá sobreposição de pombos em casas. Retorna True se houver mais pombos que casas.

🎯 Probabilidade Condicional
python
Copiar
Editar
def probabilidade_condicional(p_a_e_b, p_b):
    return p_a_e_b / p_b
Calcula P(A|B) usando:
Fórmula: P(A|B) = P(A ∩ B) / P(B)

🔁 Relação de Recorrência – Fibonacci
python
Copiar
Editar
def relacao_de_recorrencia_fibonacci(n):
    ...
Calcula o n-ésimo termo da sequência de Fibonacci.
Relação: F(n) = F(n-1) + F(n-2)

📈 Estatística: Média, Variância, Desvio Padrão
python
Copiar
Editar
def media(lista)
def variancia(lista)
def desvio_padrao(lista)
Executa cálculos estatísticos simples.
Fórmulas:

Média: μ = (soma dos valores) / n

Variância: σ² = Σ(x - μ)² / n

Desvio padrão: σ = √variância

📋 Como Usar o Programa
Ao executar, o programa exibe o menu:

markdown
Copiar
Editar
--- SISTEMA DE ANÁLISE COMBINATÓRIA E ESTATÍSTICA ---
1. Permutação
2. Combinação
3. Princípio das Casas de Pombo
4. Probabilidade Condicional
5. Relação de Recorrência (Fibonacci)
6. Análise Estatística
0. Sair
Cada opção solicita os dados necessários e retorna o resultado diretamente no terminal.

🧪 Exemplos de Uso
Permutação
Entrada: n = 5
Saída: Permutação: 120

Combinação
Entrada: n = 6, p = 2
Saída: Combinação: 15

Estatística
Entrada: 10,20,30
Saída: Média: 20.0 | Variância: 66.66... | Desvio Padrão: 8.16...
