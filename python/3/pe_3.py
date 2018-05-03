# The prime factors of 13195 are 5, 7, 13 and 29.
#
# What is the largest prime factor of the number 600851475143 ?

def get_primes(limit):
    a = [True] * limit  # Initialize the primality list
    a[0] = a[1] = False

    for (i, isprime) in enumerate(a):
        if isprime:
            yield i
            for n in range(i * i, limit, i):  # Mark factors non-prime
                a[n] = False


primes = list(get_primes(10000))
primes.insert(0,2)
primes.insert(2,5)
print(primes)

def get_factors(i):
    factors = []
    if i != 1:
        for j in primes:
            if i % j == 0:
                # print("i: ", i, " j: ", j, " i/j=", i/j)
                factors.append(j)
                factors.extend(get_factors(i / j))
                break
    return factors

print(get_factors(600851475143))