

import math


num_1 = 3
num_2 = 3.14
print(type(num_1))
print(type(num_2))

print(3 + 2)
print(3 - 2)
print(3 * 2)
print(3 / 2)
print(3 // 2)  # Floor Division
print(3 ** 2)
print(3 % 2)
print(-25 % 4)  # Positive Reminder
print(-25 % -4)  # Negative Reminder

num_3 = 1
print(num_3)
num_3 += 1
print(num_3)
num_3 *= 2
print(num_3)
print(abs(-3))
print(round(3.75))
print(round(3.75, 1))
print(3 == 3)
print(3 != 3)

num_4 = '1000'
num_5 = '2000'
print(int(num_4) + int(num_5))
num_6 = 1000
num_7 = 2000
print(str(num_6) + str(num_7))


# O(log n)
def gcd(a, b):
    if b == 0:
        return a
    return gcd(b, a % b)


print()
print(gcd(1001, 144))
print()


# Sieve of Eratosthenes for find all prime numbers up to n
# O(n * log log n)
def sieveOfEratosthenes(n):
    timer = 0
    primes = list(range(0, n + 1))
    indexes = [1] * (n + 1)
    indexes[0], indexes[1] = 0, 0
    for i in range(0, math.floor(math.sqrt(n))):
        if indexes[i] == 1:
            j = 2
            while i * j <= n:
                indexes[i * j] = 0
                timer += 1
                j += 1
    result = list()
    for i, ind in enumerate(indexes):
        if ind == 1:
            result.append(primes[i])
    return result, timer


# timer ~= 2 * n
print(sieveOfEratosthenes(1000000)[1])


# this manipulated version has O(n), but requires more spaces to store value
# however, this version also gives the factorization of n
def manipulatedSeive(n):
    timer = 0
    primes = list()
    smallest_prime_factor = [0] * (n + 1)
    for i in range(2, n + 1):
        if smallest_prime_factor[i] == 0:
            primes.append(i)
            timer += 1
            smallest_prime_factor[i] = i
        j = 0
        while j < len(primes) and primes[j] <= smallest_prime_factor[i] and i * primes[j] <= n:
            smallest_prime_factor[i * primes[j]] = primes[j]
            timer += 1
            j += 1
    return primes, timer


# timer ~= n
print(manipulatedSeive(1000000)[1])


# O(sqrt n)
def prime_factorization(n):
    i = 2
    result = list()
    while i <= math.floor(math.sqrt(n)):
        while n % i == 0:
            n = int(n / i)
            result.append(i)
        i += 1
    if n != 1:
        result.append(n)
    return result


print(prime_factorization(1001))
print(prime_factorization(14400))
print(prime_factorization(1001001))
