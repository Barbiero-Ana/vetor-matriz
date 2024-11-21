'''
4 - Crie um algorimo que informe qual o menor e o maior número em uma matriz 6x3
'''

matriz = []

for i in range(6):
    linha = []
    for x in range(3):
        num = int(input(f'Digite os números para preencher as posições: [{i + 1}, {x + 1}]'))
        linha.append(num)
    matriz.append(linha)
    
menor = matriz[0][0]
maior = matriz[0][0]

for i in range(6):
    for x in range(3):
        if matriz[i][x] < menor:
            menor = matriz[i][x]
        if matriz[i][x] > maior:
            maior = matriz[i][x]
    

print(f'\nO menor número da matriz é: {menor}\n')
print(f'\nO maior número da matriz é: {maior}\n')