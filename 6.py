'''
6 - Crie um algoritmo que leia duas matrizes 2x5 e crie uma terceira matriz com a soma dos valores dos elementos de mesmo indice
'''

matriz_1 = []
matriz_2 = []

#matriz 1
for i in range(2):
    linha = []
    for x in range(5):
        num = int(input(f'Digite o valor para preencher as sequintes posições: [{i+1}, {x+1}]'))
        linha.append(num)
    matriz_1.append(linha)


#Matriz 2
for i in range(2):
    linha = []
    for x in range(5):
        num = int(input(f'Digite o valor para preencher as sequintes posições: [{i+1}, {x+1}]'))
        linha.append(num)
    matriz_2.append(linha)

matriz_soma = []

for i in range(2):
    linha = []
    for x in range(5):
        soma = matriz_1[i][x] + matriz_2[i][x]
        linha.append(soma)
    matriz_soma.append(linha)


print(f'\nPrimeira matriz\n ')
for linha in matriz_1:
    print(linha)
    
print(f'\nSegunda matriz\n')
for linha in matriz_2:
    print(linha)
    
print(f'\nTerceira matriz\n')
for linha in matriz_soma:
    print(linha)