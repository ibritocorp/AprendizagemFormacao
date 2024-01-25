# Demonstração da importação de bibliotecas (módulos) Random e Emoji e uso das mesmas

import random
import emoji
num = random.random()
print(num)

num1 = random.randint(1, 100)
print(num1)

print(emoji.emojize("Python é TOP :thumbsup:", language='alias'))
print(emoji.emojize("Olá, Mundo :earth_americas:", language='alias'))
