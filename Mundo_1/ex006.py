# Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raíz quadrada.

numero = int(input("Digite aqui o seu número "))

print("O seu número é {}, o dobro do seu número é {} e o triplo é {}. \nA raíz quadrada é {:.2f}".format(numero, (numero*2), (numero*3), (numero**(1/2))))