#faça um programa que leia um angulo qualquer e mostre na tela o valor do seno
#cosseno e tangente desse angulo
import math
ang = float(input('Digite um angulo qualquer: '))
rad = math.radians(ang)

print('O cosseno de {}° é {} '.format(ang,math.cos(rad)))
print('O seno de {}° é {} '.format(ang,math.sin(rad)))
print('A tangente de {}° é {} '.format(ang,math.ceil(math.tan(rad))))
