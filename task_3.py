# Words combination
# Create a program that reads an input string
# and then creates and prints 5 random strings
# from characters of the input string.
# For example, the program obtained the word ‘hello’,
# so it should print 5 random strings(words)
# that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
# Tips: Use random module to get random char from string)

import random

collect_words = []

basic_word = input('Введіть своє слово: ')
word_list = list(basic_word.lower())

while len(collect_words) < 5:
    random.shuffle(word_list)
    one_word = ''.join(word_list)
    if (one_word not in collect_words) and (one_word != basic_word):
        collect_words.append(one_word)

print(*collect_words)
