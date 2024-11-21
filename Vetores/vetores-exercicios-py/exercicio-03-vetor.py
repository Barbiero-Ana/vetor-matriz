'''
3 - Escreva um algoritmo que leia um vetor com 8 posições de números 
inteiros. Em seguida, leia um novo valor do usuário e verifique se valor 
se encontra no vetor. Se estiver, informe a posição desse elemento no 
vetor. Caso o elemento não esteja no vetor, apresente uma mensagem 
informando “O número não se encontra no vetor”
'''

vetor = [int(input("Digite o valor do vetor: ")) for _ in range(8)]

verif = int(input("Digite um valor a ser verificado: "))

if verif in vetor:
    posit = vetor.index(verif)
    print(f'O valor {verif} está no vetor e sua posição é: {posit} dentro do vetor.. (Lembre-se que começa em 0)')

else:
    print(f'O valor não encontra-se  no vetor...')
