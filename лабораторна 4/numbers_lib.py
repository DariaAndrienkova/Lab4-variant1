def is_prime (n):
    if n < 2:
        return False
    for d in range(2, n):
        if n % d == 0:
            return False
    return True

def digit_sum(n):
    s = 0
    while n > 0:
        s = s + n % 10
        n = n // 10
    return s

def digits(n):
    if n == 0:
        return [0]
    result = []
    while n > 0:
        result.append(n % 10)
        n = n // 10
    result_reverse = []
    for i in range(len(result) - 1, -1, -1):
        result_reverse.append(result[i])
    return result_reverse

def first_divisor(n):
    if n < 2:
        return None
    for d in range(2, n):
        if n % d == 0:
            return d
    return None

def primes_in(lst):
    result = []
    for n in lst:
        if is_prime(n):
            result.append(n)
    return result