## Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
## biblioteca que mostra isso

import math

angulo = float(input('Digite o ângulo que você deseja: '))
seno = math.sin(math.radians(angulo))
coseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}\nO ângulo de {angulo} tem o COSSENO de {coseno:.2f}\nO ângulo de {angulo} tem a TANGENTE de {tangente:.2f}')