'''
2 - Escreva um algoritmo que leia um vetor com 15 posições de 
números inteiros. Em seguida, escreva somente os números positivos 
que se encontram no vetor.

'''

vetor = []

for i in range(15):
    num = int(input(f'Digite um valor a ser adicionado no vetor: '))
    vetor.append(num)

for num in vetor:
    if num >= 0:
        print(f'O valores positivos do vetor são: {num}')