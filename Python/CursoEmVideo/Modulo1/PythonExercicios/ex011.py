# Leia a altura e largura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária sabnedo que cada litro de tinta cobre uma área de 2m²

alt = float(input('Insira a altura da parede: '))
larg = float(input('Insira a largura da parede: '))
qtd = (alt * larg) / 2
print(f'Você precisa de {qtd:.2f}l de tinta para pintar a parede!')
