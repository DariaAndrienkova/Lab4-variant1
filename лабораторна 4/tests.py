from numbers_lib import is_prime, digit_sum, digits, first_divisor, primes_in

assert is_prime(2) == True
assert is_prime(7) == True
assert is_prime(1) == False
assert is_prime(0) == False
assert digit_sum(4821) == 15
assert digit_sum(0) == 0
assert digit_sum(123) == 6
assert digits(1234) == [1, 2, 3, 4]
assert digits(0) == [0]
assert digits(5) == [5]
assert first_divisor(6) == 2
assert first_divisor(15) == 3
assert first_divisor(1) == None
assert first_divisor(0) == None
assert primes_in([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [2, 3, 5, 7]
assert primes_in([]) == []
assert primes_in([4, 6, 8]) == []

print("Усі перевірки пройдено!")