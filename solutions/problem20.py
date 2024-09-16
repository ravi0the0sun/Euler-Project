def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum = sum + n % 10
        n = n // 10

    return sum

print(sum_of_digits(factorial(100)))