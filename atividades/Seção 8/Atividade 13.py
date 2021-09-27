"""
Obs: Sou iniciante na programção e gostaria de ir registrando meu progresso


Uma função que receba dois valores (km) e o simbolo da operação que o cliente deseja
fazer para verificar se seu carro esta bebendo demais

Obs: criterio para saber se o carro é bom ou não:
Consumo menor que 8 "venda o carro"
entre 8 e 14 "Econômico"
acima de 14 "Super econômico"
"""


def consumo(num1=0, num2=0):
    result = ""   # Resultado que sera usado mais abaixo para o resultado dasoperações

    def venda():  # Função que vai verificar se o carro esta consumindo muito
        if result < 8:
            return 'venda o carro'
        elif 8 >= result <= 14:
            return "Econômico"
        return 'Super econômico'
        # print que exibira os sinais que deseja calcular
    print("Sinais das operações:"
          '\n'
          "/ = Divisão"
          '\n'
          "+ = Soma"
          '\n'
          "- = Subtração"
          '\n'
          "* =  Multiplicação")
    "\n"
    # abaixo: input para o sinal da operação desejada
    sinal = input('Digite o sinal da operação: ')
    # abaixo: Condição dependendo do sinal digitado pelo usuário
    # vai realizar a operação e retornar o print
    if sinal == "/":
        result = num1 / num2
        return f"o carro esta fazendo {result} KM por litros {venda()}"
    elif sinal == "+":
        result = num1 + num2
        return f"o carro esta fazendo {result} KM por litros {venda()}"
    elif sinal == "-":
        result = num1 - num2
        return f"o carro esta fazendo {result} KM por litros {venda()}"
    elif sinal == "*":
        result = num1 * num2
        return f"o carro esta fazendo {result} KM por litros {venda()}"
    else:
        # Abaixo: repetição caso o usuário digite um valor que não faça parte
        # dos sinais
        while sinal != "/" and sinal != "+" and sinal != "-" and sinal != "-":
            sinal = input('Digite o sinal CORRETO da operação: ')
            if sinal == "/":
                result = num1 / num2
                return f"o carro esta fazendo {result} KM por litros {venda()}"
            elif sinal == "+":
                result = num1 + num2
                return f"o carro esta fazendo {result} KM por litros {venda()}"
            elif sinal == "-":
                result = num1 - num2
                return f"o carro esta fazendo {result} KM por litros {venda()}"
            elif sinal == "*":
                result = num1 * num2
                return f"o carro esta fazendo {result} KM por litros {venda()}"


numeros1 = int(input("Digite o valor dos Quilometros: "))
numeros2 = int(input("Digite o valor dos Litros: "))

print(consumo(numeros1, numeros2))
