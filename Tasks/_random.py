def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def is_complex(num):
    for i in range(2, num):
        if num % i == 0:
            return True
    return False


def generate_permutation(n):
    if n <= 2:
        return [-1]

    permutation = list(range(1, n + 1))

    for i in range(n - 1):
        if is_complex(sum(permutation[:i+1])):
            permutation[i], permutation[i+1] = permutation[i+1], permutation[i]

    if is_complex(sum(permutation)):
        return permutation
    else:
        return [-1]


n1 = 3
result1 = generate_permutation(n1)
print(*result1)

n2 = 4
result2 = generate_permutation(n2)
print(*result2)
