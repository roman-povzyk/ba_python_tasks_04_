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

user_answer = input(f'{a} {operation} {b} = ')

while not user_answer.isdigit():
    user_answer = input(f'Будь ласка, введіть відповідь: ')

if int(user_answer) == computer_answer:
    print(f'Так, {int(user_answer)} — правильна відповідь!')
else:
    if int(user_answer) > computer_answer:
        print(f'Вибачте, але ви помилилися. Відповідь на {int(user_answer) - computer_answer} менше.')
    else:
        print(f'Вибачте, але ви помилилися. Відповідь на {computer_answer - int(user_answer)} більше.')
