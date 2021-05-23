# The math quiz program
# Write a program that asks the answer
# for a mathematical expression,
# checks whether the user is right or wrong,
# and then responds with a message accordingly.

import random

a = random.randint(1, 10)
b = random.randint(1, 10)
operation_list = ['+', '-', '*']
operation = random.choice(operation_list)

if operation == '+':
    computer_answer = a + b
elif operation == '-':
    computer_answer = a - b
else:
    computer_answer = a * b

user_answer = int(input(f'{a} {operation} {b} = '))

if user_answer == computer_answer:
    print(f'Так, {user_answer} — правильна відповідь!')
else:
    if user_answer > computer_answer:
        print(f'Вибачте, але ви помилися. Відповідь на {user_answer - computer_answer} менше.')
    else:
        print(f'Вибачте, але ви помилися. Відповідь на {computer_answer - user_answer} більше.')
