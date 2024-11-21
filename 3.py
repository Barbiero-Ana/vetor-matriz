'''
3 - Crie um algoritmo que leia a média dos elementos de uma matriz 5x2
'''

matriz = []

for i in range(5):
    linha = []
    for x in range(2):
        num = int(input(f'Digite os valores para preencher as posições: [{i + 1}, {x + 1}]'))
        linha.append(num)
    matriz.append(linha)
    
print('\nPreenchimento completo!\n')

soma = 0
for i in range(5): #linhas
    for x in range(2): #colunas
        soma += matriz[i][x]
print(f'valor total da soma: {soma}')
total = 5 * 2
media = soma / total

print(f'\nA média dos elementos será de: {media}\n')    