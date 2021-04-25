def get_primes(n):
    return [x
            for x in range(2, n + 1)
            if all(x % y != 0 for y in range(2, x // 2 + 1))]

