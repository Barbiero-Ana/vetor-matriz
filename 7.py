'''
7 - Crie um algoritmo que calcule a soma  dos valores da diagonal principal de uma matrix 5x5
'''

matriz = []

for i in range(5):
    linha = []
    for x in range(5):
        num = int(input(f'Digite os valores a serem preenchidos nas posições: [{i + 1}, {x + 1}]'))
        linha.append(num)
    matriz.append(linha)

soma_d = 0

for i in range(5):
    soma_d += matriz[i][i] # A posição da diagonal principal é [i][i]

print(f'\nA soma das diagonais será: {soma_d}\n')