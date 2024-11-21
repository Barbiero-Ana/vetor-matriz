'''
9 - Crie um algoritmo que verifica se a matriz é uma triangular inferior - Para isto, todos os elementos acima da diagonal principal são iguais a 0
'''

matriz = []

for i in range(5):
    linha = []
    for x in range(5):
        num = int(input(F'Digite os valores a preencherem as seguintes posições: [{i + 1}, {x + 1}]'))
        linha.append(num)
    matriz.append(linha)

inferior = True

for i in range(5):
    for y in range(i + 1, 5): # A coluna precisa ser maior que a linha para estar acima da diagonal
        if matriz[i][y] != 0:
            inferior = False
            break
    if not inferior:
        break
    
if inferior:
    print('\nA matriz é uma triangular inferior.\n')
    
else:
    print('\nA matriz não é uma triangular inferior.\n')