## faça um programa que leia três números e mostre qual é o maior e qual é o menor

a = int(input("Primeiro valor: "))
b = int(input("Segundo valor: "))
c = int(input("Terceiro valor: "))
# Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# Verificando quem é o maior
maior = b
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print("O menor valor digitando foi {}".format(menor))