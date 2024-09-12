with open('./prob11_input.txt') as file:
    data = file.readlines()

matrix = []

for line in data:
    row = list(map(int, line.split()))
    matrix.append(row)
        

print(matrix)