#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

metro = int(input("Digite aqui quantos metros você deseja: "))
cm = metro * 100
mm = metro * 1000
print("A média de {} convertida em {}cm e {}mm".format(metro, cm, mm))