from numbers_lib import is_prime, digit_sum, digits, first_divisor, primes_in

def main():
    n = int(input("Введіть ціле невід'ємне число: "))

    print("Число є простим:", is_prime(n))
    print("Сума цифр числа:", digit_sum(n))
    print("Список цифр числа:", digits(n))
    print("Найменший дільник (більший за 1):", first_divisor(n))

    numbers = [1, 2, 3, 4, 5, 11, 12, 13, 17, 20]
    print("Знайдені прості числа зі списку:", primes_in(numbers))

if __name__ == "__main__":
    main()