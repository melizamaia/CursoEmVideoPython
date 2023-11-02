##Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

temperatura_c = float(input("Digite a temperatura em °C: "))
temperatura_f = ((9*temperatura_c)/5)+32
print("A temperatura de {}°C corresponde a {}°F".format(temperatura_c, temperatura_f))