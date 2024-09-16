def factorial(n):
    if n == 1:
        return n
    return n * factorial(n - 1)

def sum_of_digits(n):
    if n > 0:
        return n % 10 + sum_of_digits(n // 10)
    return n

print(sum_of_digits(factorial(100)))