'''
4 - Escreva um algoritmo que leia dois vetores de 10 posições e faça a 
soma dos elementos de mesmo índice, colocando o resultado em um 
terceiro vetor. Mostre o vetor resultante.
'''

vetor1 = [int(input("Digite um valor a ser adicionado ao primeiro vetor: ")) for _ in range(10)]

vetor2 = [int(input("Digite um valor a ser adicionado ao segundo vetor: ")) for _ in range(10)]

soma = []

for i in range(10):
    soma.append(vetor1 [i]+ vetor2[i])
    
print(f'O vetor resultante será: {soma}')