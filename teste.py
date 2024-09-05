#1) Observe o trecho de código abaixo: int INDICE = 13, SOMA = 0, K = 0; Enquanto K < INDICE faça { K = K + 1; SOMA = SOMA + K; } Imprimir(SOMA); Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0
k = 0
while k < indice:
     k = k + 1
     soma = soma + k
     print(soma) 
"""
1
3
6
10
15
21
28
36
45
55
66
78
91
"""

"""2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número, ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

IMPORTANTE: Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;"""
def fibonacci(): #função que gera a sequencia de fibonacci 
    sequencia = [0,1] # Sequencia recebe os números de fibonacci
    while len(sequencia) < 40: #loop para formar a sequência com 40 unidades
        sequencia.append(sequencia[-1] + sequencia[-2])
    return(sequencia)  
       

def verifica(numero): # Função que verifica se o número digitado pelo usuário está dentro de sequencia
  sequencia = fibonacci() #Chama a função fibonacci e coloca o retorno na variável interna sequencia
  if numero in sequencia: #verifica se o numero está dentro da lista
    print(f"O número {numero} está na sequência de Fibonacci!!! Uhhuuuu")
  else:
    print(f"O número não está na sequência de Fibonacci!!! Vamos tentar outro?")

numero = int(input("Digite um número até 47000 para verificar se está na sequência de fibonacci"))
print(verifica(numero))

"""
Exemplo de saída
Digite um número até 47000 para verificar se está na sequência de fibonacci1
[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946, 17711, 28657, 46368, 75025, 121393, 196418, 317811, 514229, 832040, 1346269, 2178309, 3524578, 5702887, 9227465, 14930352, 24157817, 39088169, 63245986]
40
O número 1 está na sequência de Fibonacci!!! Uhhuuuu
"""

#3) Dado um vetor que guarda o valor de faturamento diário de uma distribuidora, faça um programa, na linguagem que desejar, que calcule e retorne: • O menor valor de faturamento ocorrido em um dia do mês; • O maior valor de faturamento ocorrido em um dia do mês; • Número de dias no mês em que o valor de faturamento diário foi superior à média mensal.
#IMPORTANTE: a) Usar o json ou xml disponível como fonte dos dados do faturamento mensal; b) Podem existir dias sem faturamento, como nos finais de semana e feriados. Estes dias devem ser ignorados no cálculo da média;

valores = [
	{
		"dia": 1,
		"valor": 22174.1664
	},
	{
		"dia": 2,
		"valor": 24537.6698
	},
	{
		"dia": 3,
		"valor": 26139.6134
	},
	{
		"dia": 4,
		"valor": 0.0
	},
	{
		"dia": 5,
		"valor": 0.0
	},
	{
		"dia": 6,
		"valor": 26742.6612
	},
	{
		"dia": 7,
		"valor": 0.0
	},
	{
		"dia": 8,
		"valor": 42889.2258
	},
	{
		"dia": 9,
		"valor": 46251.174
	},
	{
		"dia": 10,
		"valor": 11191.4722
	},
	{
		"dia": 11,
		"valor": 0.0
	},
	{
		"dia": 12,
		"valor": 0.0
	},
	{
		"dia": 13,
		"valor": 3847.4823
	},
	{
		"dia": 14,
		"valor": 373.7838
	},
	{
		"dia": 15,
		"valor": 2659.7563
	},
	{
		"dia": 16,
		"valor": 48924.2448
	},
	{
		"dia": 17,
		"valor": 18419.2614
	},
	{
		"dia": 18,
		"valor": 0.0
	},
	{
		"dia": 19,
		"valor": 0.0
	},
	{
		"dia": 20,
		"valor": 35240.1826
	},
	{
		"dia": 21,
		"valor": 43829.1667
	},
	{
		"dia": 22,
		"valor": 18235.6852
	},
	{
		"dia": 23,
		"valor": 4355.0662
	},
	{
		"dia": 24,
		"valor": 13327.1025
	},
	{
		"dia": 25,
		"valor": 0.0
	},
	{
		"dia": 26,
		"valor": 0.0
	},
	{
		"dia": 27,
		"valor": 25681.8318
	},
	{
		"dia": 28,
		"valor": 1718.1221
	},
	{
		"dia": 29,
		"valor": 13220.495
	},
	{
		"dia": 30,
		"valor": 8414.61
	}
]
# Filtra valores zerados
valores_filtrados = [(dia["dia"],dia["valor"]) for dia in valores if dia["valor"] > 0]
# Pega o dia e o menor valor
menor_dia , menor_valor = min(valores_filtrados, key=lambda x: x[1])
# Pega o dia e maior valor
maior_dia , maior_valor = max(valores_filtrados, key=lambda x: x[1])
# Tira a média
media = round(sum(valor for _, valor in valores_filtrados) / len(valores_filtrados), 2)
# Soma os dias acima da média 
dias_acima_da_media = sum(1 for _, valor in valores_filtrados if valor > media)

print("-------------------------------------------------------")
print(f"O menor faturamento encontrado foi no dia {menor_dia} com o valor de R${round(menor_valor,2)}.")
print(f"O maior faturamento foi no dia {maior_dia} com o faturamento de R${round(maior_valor,2)}.")
print(f"A média de faturamento mensal ficou em R${media}.")
print(f"O total de dias acima da média foi de {dias_acima_da_media} dia/s")
print("-------------------------------------------------------")

""" 
Resultado esperado
-------------------------------------------------------
O menor faturamento encontrado foi no dia 14 com o valor de R$373.78.
O maior faturamento foi no dia 16 com o faturamento de R$48924.24.
A média de faturamento mensal ficou em R$20865.37.
O total de dias acima da média foi de 10 dia/s
-------------------------------------------------------
"""
#4) Dado o valor de faturamento mensal de uma distribuidora, detalhado por estado: • SP – R 67.836,43∙RJ–R 36.678,66 • MG – R 29.229,88∙ES–R 27.165,48 • Outros – R$19.849,53
#Escreva um programa na linguagem que desejar onde calcule o percentual de representação que cada estado teve dentro do valor total mensal da distribuidora. 

# Coloquei em dicionário para facilitar
faturamento = [
    {"estado": "SP", "valor": 67836.43},
    {"estado": "RJ", "valor": 36678.66},
    {"estado": "MG", "valor": 29229.88},
    {"estado": "ES", "valor": 19849.53}
]
# Soma o faturamento total da empresa.
total_mensal = sum(item["valor"] for item in faturamento)
print(f"O total de faturamento foi de R${total_mensal}.")
# Loop para iterar dentro do dicionário e retirar a porcentagem de cada estado.
for item in faturamento:
    percentual = (item["valor"] / total_mensal) * 100
    # Imprime cada estado e sua porcentagem.
    print(f"O estado de {item['estado']} representa {percentual:.2f}% dentro do total da empresa.")
"""
Exemplo da saída
O total de faturamento foi de R$153594.5.
O estado de SP representa 44.17% dentro do total da empresa.
O estado de RJ representa 23.88% dentro do total da empresa.
O estado de MG representa 19.03% dentro do total da empresa.
O estado de ES representa 12.92% dentro do total da empresa.
"""    

#5) Escreva um programa que inverta os caracteres de um string.
#IMPORTANTE: a) Essa string pode ser informada através de qualquer entrada de sua preferência ou pode ser previamente definida no código; b) Evite usar funções prontas, como, por exemplo, reverse;

# Pede ao usuário para digitar uma frase
frase = input("Digite uma frase que queira inverter: ")
# Usa o método de fatiamento para começar de trás e ir imprimindo com o print.
print(frase[::-1])
"""
Exemplo de saída.
Digite uma frase que queira inverter: Quero comer boloooo!
!oooolob remoc oreuQ
"""