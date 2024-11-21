'''
Criar um algoritmo que leia 10 números pelo teclado e exiba os números
na ordem inversa da que os números foram digitados.
'''
vetor = [int(input("Digite um valor: ")) for _ in range(10)]

print(vetor[::-1])    
