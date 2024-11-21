'''
5 - Crie um algoritmo que leia um vetor de 20 posições e informe:
a)Quantos números pares existem no vetor
b)Quantos números ímpares existem no vetor
c)Quantos números maiores do que 50
d)Quantos números menores do que 7

'''

vetor = []

for i in range(20):
    numero = int(input(f"Digite o número na posição {i+1}: "))
    vetor.append(numero)

# Inicializando contadores
pares = 0
impares = 0
maiores_que_50 = 0
menores_que_7 = 0

# Processando o vetor
for numero in vetor:
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 50:
        maiores_que_50 += 1
    
    if numero < 7:
        menores_que_7 += 1

# Exibindo os resultados
print(f"Quantidade de números pares: {pares}")
print(f"Quantidade de números ímpares: {impares}")
print(f"Quantidade de números maiores que 50: {maiores_que_50}")
print(f"Quantidade de números menores que 7: {menores_que_7}")
