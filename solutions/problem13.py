

DIGIT_LEN = 100

with open('../input_files/prob13_input.txt') as fi:
    input = fi.read().strip().replace('\n', ',').split(',')
    array = [int(n_string) for n_string in input]

sum = 0
for n in array:
    sum += n

print(str(sum)[:10])