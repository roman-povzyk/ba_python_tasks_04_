# The Guessing Game.
# Write a program that generates a random number between
# 1 and 10 and lets the user guess what number was generated.
# The result should be sent back to the user via a print statement.

import random

user_number = int(input('Введіть число від 1 до 10: '))
computer_number = random.randint(1, 10)

if user_number == computer_number:
    print(f'Вітаю, ви вгадали! Це число {user_number}.')
else:
    if user_number > computer_number:
        print(f'Вибачте, але ви не вгадали. Ваше число було на {user_number - computer_number} більше.')
    else:
        print(f'Вибачте, але ви не вгадали. Ваше число було на {computer_number - user_number} менше.')