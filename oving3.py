import math


def is_prime(n):
    if n == 2:
        return True
    if n < 2 or (n % 2 == 0):
        return False

    for i in range(3, math.floor(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


def find_n_primes(n):
    number = 0
    prime_count = 0

    while prime_count < n:
        if is_prime(number):
            prime_count += 1
            print(number)
        number += 1


find_n_primes(1000)
