## Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome. (primeiro e o último)
nome = str(input("Digite aqui seu nome: ")).strip()
print("Seu nome tem Silva? {}".format("SILVA" in nome.upper()))