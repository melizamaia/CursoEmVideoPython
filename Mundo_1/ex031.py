## Desenvolva um programa que pergunte a distância de uma viagem em km.
## Calcule o preço da passage, cobrando R$0,50 por Km para viagens de até 200KM e R%0,45 para viagens mais longas

distancia = float(input("Qual é a distância da sua viagem? "))
print("Você está prestes a começar uma viagem de {}km".format(distancia))
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print("E o preço da sua passagem será de R${:.2f}".format(preco))