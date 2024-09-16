ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ALPHA_VALUE = {}

for i, letter in enumerate(list(ALPHABET)):
    ALPHA_VALUE |= {letter: i + 1}

with open('../input_files/prob22_input.txt') as fi:
    input_data = sorted(fi.read().strip().replace('"', '').split(','))

sum = 0
for index, name in enumerate(input_data):
    value = 0
    for letter in list(name):
        value = value + ALPHA_VALUE[letter]
    sum = sum + ((index + 1) * value)

print(sum)