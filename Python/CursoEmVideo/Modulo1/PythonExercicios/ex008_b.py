# Leia um valor em metros e imprima na tela os equivalentes da unidade 'metro'

n = float(input('Insira o valor em metros: '))
km = 'km'
hm = 'hm'
dam = 'dam'
m = 'm'
dm = 'dm'
cm = 'cm'
mm = 'mm'
print(f'{km:*^20}{hm:*^20}{dam:*^20}{m:*^20}{dm:*^20}{cm:*^20}{mm:*^20}')
print(f'{n / 1000:*^20}{n / 100:*^20}{n / 10:*^20}{n:*^20}{n * 10:*^20}{n * 100:*^20}{n * 1000:*^20}')
