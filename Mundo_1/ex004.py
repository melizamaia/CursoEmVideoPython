#Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele

teste = str(input("Digite algo no seu teclado: "))
print("O tipo primitivo desse valor é ", type(teste))
print("Só tem espaços? ", teste.isspace())
print("É um numero? ", teste.isnumeric())
print("É alfabético? ", teste.isalpha())
print("É alfanumérico?", teste.isalnum())
print("Está em maiúsculas? ", teste.isupper())
print("Está em minúsculas? ", teste.islower())
print("Está capitalizada? ", teste.istitle())