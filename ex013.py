#Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.

##Aguardando a correção do 12 para entender melhor o 13

salario = float(input("Digite aqui o seu salário: R$"))
aumento = salario + (salario * 15 / 100)

print("O seu salário é R${:.2f} e com o aumento fica no valor de R${:.2f}".format(salario, aumento))