'''
1 - Crie um algoritmo que leia uma matriz 5x5. Em seguida conte quantos numeros pares existem na matriz
'''

matriz = []

for i in range(5):
    linha = []
    for x in range(5):
        num = int(input(f'Digite o valor para as seguintes posições: [{i + 1}, {x + 1}]'))
        linha.append(num)
    matriz.append(linha)
    
print('\nPreenchimento completo!\n')

n_par = 0

for i in range(5):
    for x in range(5):
        if matriz[i][x] % 2 == 0: 
            n_par += 1

print(f'Existem {n_par} números pares na matriz.')