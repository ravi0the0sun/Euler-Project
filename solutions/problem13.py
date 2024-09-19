DIGIT_LEN = 100

with open('../input_files/prob13_input.txt') as fi:
    input = fi.read().strip().replace('\n', ',').split(',')

sum = 0
for n in input:
    sum += int(n)

print(''.join(list(str(sum))[:10]))