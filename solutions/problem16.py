POWER = 1000

def sum_of_digit(n):
    square = 2 ** n
    t = 0
    while square > 0:
        t = t + square % 10
        square = square // 10

    return t

print(sum_of_digit(POWER))