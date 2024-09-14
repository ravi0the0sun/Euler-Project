import timeit

STARTING_N = 1000000

def longest_chain(n):
    long_len = 1  
    number = 1
    def count_chain(n):
        length = 1
        while n > 1:
            if n % 2 == 0:
                n = n // 2
                length += 1
            else:
                n = 3 * n + 1
                length += 1
        return length
    
    while n > 1:
        count = count_chain(n)
        if count > long_len:
            long_len = count
            number = n
            n -= 1
        else:
            n -= 1

    return number


print(timeit.timeit('print(longest_chain(STARTING_N))', globals=globals(), number=1))

        