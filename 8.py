'''
8 - Crie um algorito que verifica se uma matriz é triangular superior - Uma matriz é considerada triangular superior se todos os elementos abaixo da diagonal principal são iguais a 0
'''

matriz = []

for i in range (5):
    linha = []
    for x in range(5):
        num = int(input(f'Digite os números a preencherem as seguintes posições: [{i + 1}, {x + 1}]'))
        linha.append(num)
    matriz.append(linha)

superior = True

for i in range(1, 5):
    for y in range(i):
        if matriz[i][y] != 0: # A coluna precisa ser menor que a linha para estar abaixo da diagonal
            superior = False
            break
    if not superior:
        break
    
if superior:
    print('\nA matriz é uma triangular superior.\n')
    
else:
    print('A matriz não é uma triangular superior.')