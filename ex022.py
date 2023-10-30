## Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas. (2)
## Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = str(input("Digite seu nome completo: ")).strip() ##não contas os espaços
print("Analizando seu nome...")
print("Seu nome em letras maiúsculas é {}".format(nome.upper()))
print("Seu nome em letras minúsuculas é {}".format(nome.lower()))
print("Seu nome tem ao todo {} letras".format(len(nome)-nome.count(' '))) ## menos o contador de espaços
print("Seu primeiro nome tem {} letras".format(nome.find(' ')))