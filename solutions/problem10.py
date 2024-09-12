import timeit

def sum_of_prime(n):
    sum = 0
    def is_prime(i):
        if i == 1:
            return False
        p = 2
        while i > p:
            if i % p == 0: 
                return False
            p += 1
        return True
    while n > 0:
        if is_prime(n):
            sum = sum + n
            n -= 1
        else:
            n -= 1
    return sum

print(timeit.timeit('print(sum_of_prime(2000000))', globals = globals(), number = 1))
