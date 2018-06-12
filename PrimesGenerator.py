import itertools

def isPrime(x):
    if x == 2 or x == 3:
        return True

    if x % 2 == 0 or x % 3 == 0:
        return False

    i = 5
    w = 2
    while i * i <= x:
        if x % i == 0:
            return False

        i += w
        w = 6 - w

    return True

def primes():
    x = 1
    while True:
        x += 1
        if isPrime(x):
            yield x

def primes1():
    x = 1
    i = 5
    w = 2
    while True:
        x += 1
        if x == 2 or x == 3:
            yield x

        if x % 2 == 0 or x % 3 == 0:
            continue

        isPrime = True
        while i * i <= x:
            if x % i == 0:
                isPrime = False
                break

            i += w
            w = 6 - w

        if isPrime:
            yield x

print(list(itertools.takewhile(lambda x: x <= 31, primes())))

