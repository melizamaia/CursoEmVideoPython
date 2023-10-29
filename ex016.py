# Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção inteira
# Ex: Digite um número 6.127
# O número 6.127 tem a parte inteira 6
# olhar as funções do módulo math


# Utilizando o floor
import math
num = float(input("Digite um número real: "))
real = math.floor(num)
print("A porção inteira de {} é igual a {}".format(num, real))

#Utilizando o trunc
from math import trunc
num = float(input("Digite um valor: "))
print("O valor digitado foi {} e a sua porção inteira é {}".format(num, trunc(num)))

#Utilizando o básico
num = float(input("Digite aqui um número: "))
print ("O valor real foi {} e é o valor integro é igual a {}".format(num, int(num)))