#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos Dólares ela pode comprar.

#Considere
# U$1,00 = 3,27

real = float(input("Quanto dinheiro você tem na carteira? "))
dolar = real * 3.27

print("Com R${:.2f} você pode comprar U${:.2f}".format(real, dolar))