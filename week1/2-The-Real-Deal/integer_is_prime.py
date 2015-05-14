def is_prime(n):

    if n == 1:
        return False

    divisors = [x for x in range(2, n) if x != n]
    for d in divisors:
        if n % d == 0:
            return False
    return True
