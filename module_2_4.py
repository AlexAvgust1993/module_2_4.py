numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
a = 0
c = len(numbers)
for i in range(2, c + 1):
    for g in range(2, i):
        if i % g == 0:
            a += 1
    if a == 0:
        primes.append(i)
    else:
        a = 0
        not_primes.append(i)
print(primes)
print(not_primes)

