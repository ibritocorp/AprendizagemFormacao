# Definindo cores por json

cores = {'limpa':'\033[m',
         'c1':'\033[0;31;40m',
         'c2':'\033[1;31;107m'}

print(f'{cores["c1"]}Olá{cores["limpa"]}, {cores["c2"]}Mundo{cores["limpa"]}!')