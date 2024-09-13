import timeit

DIVISORS = 500

def tri_number():
    count = 0
    n = 1
    t = 1
    def count_divisior(n):
        p = 1
        d = 0
        while p <= n:
            if n % p == 0:
                d += 1
                p += 1
            else:
                p += 1
        return d
    
    while count <= DIVISORS:
        count = count_divisior(n)
        if count == DIVISORS:
            return n
            
        n = (t * (t + 1)) // 2
        t += 1

    return None
    
    
print(timeit.timeit("print(tri_number())", globals=globals(), number=1))

