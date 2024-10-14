numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
primes = []
not_primes = []
is_prime = True

for i in range(len(numbers) + 1):
    for j in range(2, i):
        if i <= 1 and j <= 0:
            continue
        if i % j == 0:
            is_prime = False
    if i <= 1:
        continue
    if is_prime:
        is_prime = True
        primes.append(i)
    else:
        is_prime = True
        not_primes.append(i)

print('Primes:', primes)
print('Not primes:', not_primes)


# это первый вариант который у меня получился, но понял что если вдруг будет в списке
# дополение значений 0 или 1, то нужно пропускать их
#
# for i in range(2, len(numbers) + 1):
#     for j in range(2, i):
#         if i % j == 0:
#             a += 1
#     if a == 0:
#         primes.append(i)
#     else:
#         a = 0
#         not_primes.append(i)
# print('Primes:', primes)
# print('Not primes:', not_primes)