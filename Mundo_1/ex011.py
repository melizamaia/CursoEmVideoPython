#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la,
#sabendo que cada litro de tinta, pinta uma área de 2m².

larg = float(input("Digite aqui o valor da largura da sua parede: "))
alt = float(input("Digite aqui o valor da altura da sua parede: "))
area = larg * alt

print("Sua parede tem a dimensão de {}x{} e sua área é de {}m².".format(larg, alt, area))

tinta = area / 2
print("Para você pintar essa parede, você precisará de {}l de tinta".format(tinta))