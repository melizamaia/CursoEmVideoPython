## Crie um programa que leia um número inteiro e mostre na teça se ele é PAR ou ÍMPAR

num = int(input("Digite aqui o seu número: "))
resultado = num % 2
if resultado == 0:
    print("O número {} é PAR".format(num))
else:
    print("O número {} é ÍMPAR".format(num))