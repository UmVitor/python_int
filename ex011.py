larg = int(input('Digite a largura da parede: '))
alt = int(input('Digite a altura da parede: '))
area = larg*alt
print('A área da parede é de {}'.format(area))
print('Para pintar essa parede é necessario {} litros de tinta'.format(area/2))