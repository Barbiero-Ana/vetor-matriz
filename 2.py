'''
2 - Crie uma matriz 3x3 e calcule a soma dos valores das colunas da matriz
'''

matriz = []

for i in range(3): #LINHAS (as linhas sempre veem primeiro)
    linha = []
    for x in range(3): #COLUNAS (as colunas veem em segundo)
        num = int(input(f'Digite o valor a preencher as posições: [{i + 1}, {x + 1}]'))
        linha.append(num)
    matriz.append(linha)
    
print('\n preenchimento completo!\n')

for x in range(3): # colunas
    soma = 0
    for i in range(3): #linhas
        soma += matriz[i][x]
    print(f'A soma da coluna {x + 1} será: {soma}')