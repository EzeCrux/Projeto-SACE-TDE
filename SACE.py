def fatorial(n):
    if n == 0 or n == 1:
        return 1
    resultado = 1
    for i in range(2, n + 1):
        resultado *= i
    return resultado

def permutacao(n):
    return fatorial(n)


def arranjo(n, p):
    return fatorial(n) // fatorial(n - p)


def combinacao(n, p):
    return fatorial(n) // (fatorial(p) * fatorial(n - p))


def principio_das_casas_de_pombo(pombos, casas):
    if pombos > casas:
        return True
    else:
        return False


def probabilidade_condicional(p_a_e_b, p_b):
    if p_b == 0:
        return "Indefinido (divisão por zero)"
    return p_a_e_b / p_b


def relacao_de_recorrencia_fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return relacao_de_recorrencia_fibonacci(
            n - 1
        ) + relacao_de_recorrencia_fibonacci(n - 2)


def media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma / len(lista)


def variancia(lista):
    m = media(lista)
    soma_quadrados = 0
    for valor in lista:
        soma_quadrados += (valor - m) ** 2
    return soma_quadrados / len(lista)


def desvio_padrao(lista):
    return variancia(lista) ** 0.5


def menu():
    while True:
        print("\n--- SISTEMA DE ANÁLISE COMBINATÓRIA E ESTATÍSTICA ---")
        print("1. Permutação")
        print("2. Combinação")
        print("3. Princípio das Casas de Pombo")
        print("4. Probabilidade Condicional")
        print("5. Relação de Recorrência (Fibonacci)")
        print("6. Análise Estatística")
        print("0. Sair")
        opcao = input("Escolha uma opção: ")
        if opcao == "1":
            n = int(input("Digite o valor de n: "))
            print("Permutação:", permutacao(n))
        elif opcao == "2":
            n = int(input("Digite o valor de n: "))
            p = int(input("Digite o valor de p: "))
            print("Combinação:", combinacao(n, p))
        elif opcao == "3":
            pombos = int(input("Digite o número de pombos: "))
            casas = int(input("Digite o número de casas: "))
            if principio_das_casas_de_pombo(pombos, casas):
                print("Pelo menos uma casa terá mais de um pombo.")
            else:
                print("Cada pombo pode ocupar uma casa sem repetição.")
        elif opcao == "4":
            p_a_e_b = float(input("Digite P(A ∩ B): "))
            p_b = float(input("Digite P(B): "))
            print("P(A|B) =", probabilidade_condicional(p_a_e_b, p_b))

        elif opcao == "5":
            n = int(input("Digite a posição n da sequência de Fibonacci: "))
            print(f"Fibonacci({n}) =", relacao_de_recorrencia_fibonacci(n))

        elif opcao == "6":
            dados = input("Digite os dados separados por vírgula: ")
            lista = [float(x.strip()) for x in dados.split(",")]
            print("Média:", media(lista))
            print("Variância:", variancia(lista))
            print("Desvio Padrão:", desvio_padrao(lista))

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")


menu()
