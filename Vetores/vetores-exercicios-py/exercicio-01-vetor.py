'''
1- Crie um algoritmo que leia um vetor de 10 números inteiros. Em 
seguida, calcule e escreva o somatório dos valores deste vetor. 

'''

vetor = [int(input("Digite um valor a ser adicionado no vetor: ")) for _ in range(10)]

soma = sum(vetor)

print(f'os vetores são:{vetor}, e a soma de seus componentes será: {soma}')
