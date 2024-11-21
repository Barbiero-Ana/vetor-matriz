'''
2 - Escreva um algoritmo que leia um vetor com 15 posições de 
números inteiros. Em seguida, escreva somente os números positivos 
que se encontram no vetor.

'''
'''
Versão usando dois vetores para armazenar os numeros positivos
'''
vetor = []

for i in range(15):
    num = int(input(f'Digite um valor a ser adicionado no vetor: '))
    vetor.append(num)

positivos = []

for num in vetor:
    if num >= 0:
        positivos.append(num)

print(f'O valores do vetor são: {vetor}, e seus valores positivos são: {positivos}')