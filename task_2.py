# The birthday greeting program.
# Write a program that takes your name as input,
# and then your age as input and greets you with the following:
# 'Hello <name>, on your next birthday you’ll be <age+1> years'

name = input('Введіть ваше ім\'я: ')
age = input('Введіть ваш вік: ')

while not age.isdigit():
    age = input('Будь ласка, введіть ваш вік числом: ')

print(f'Hello {name}, on your next birthday you’ll be {int(age) + 1} years')