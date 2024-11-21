'''
Escreva um algoritmo que leia um vetor com 10 posições de números
inteiros. Em seguida, receba um novo valor do usuário e verifique se
este valor se encontra no vetor
'''

vetor = [int(input("Digite os valores para preencher o veotr: ")) for _ in range(10)]

verificar = int(input("Digite o valor a ser verificado: "))

if verificar in vetor:
    print(f'O valor está presente no vetor![{verificar}]')
    
else:
    print(f'O valor não está presente no vetor...{verificar}')