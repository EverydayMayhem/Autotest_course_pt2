# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random
import string
def generate_random_name():
    letter_one, letter_two = "",""
    seed = string.ascii_lowercase
    # генерируем два разных слова с рандомным количеством букв
    for i, j in range(random.randint(1,15)):
        letter_one += random.choice(seed)

    for j in range(random.randint(1,15)):
        letter_two += random.choice(seed)

    result = f'{letter_one} {letter_two}'
    yield result


print(next(generate_random_name()))
print(next(generate_random_name()))
print(next(generate_random_name()))
print(next(generate_random_name()))
