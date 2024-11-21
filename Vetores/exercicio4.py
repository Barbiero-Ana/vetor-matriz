'''
As estruturas de repetição (tanto para, enquanto e repita)permitem o
uso do comando INTERROMPA
Esse comando causa a saída imediata do laço de repetição
'''

vetor = [int(input("Digite os valores do vetor: ")) for _ in range(10)]

verifica = int(input("Digite o valor que deseja verificar: "))
#Lembrar de estudar o pq do X =0 e X = 1
x = 0

for verifica in vetor:
        x = 1
        break

if x ==1:
        print(f'O valor está no vetor!')
        
else:
        print(f'O valor não está no vetor...')