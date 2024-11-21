'''
5 - Crie um algoritmo que leia uma matriz 3x3 e crie uma segunda matriz que inverta as linhas e as colunas da primeira matriz 
'''

matriz = []

for i in range(3):
    linha = []
    for x in range(3):
        num = int(input(f'Digite os valores para prencher as seguintes posições: [{i + 1}, {x + 1}]'))
        linha.append(num)
    matriz.append(linha)
    
matriz_nova = [[matriz[x][i] for x in range(3)] for i in range(3) ]

print('\nMatriz original\n')

for linha in matriz:
    print(linha)
    
print('\nNova matriz\n')

for linha in matriz_nova:
    print(linha)