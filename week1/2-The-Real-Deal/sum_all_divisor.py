def divisors(n):
    return [x for x in range(1, n + 1) if n % x == 0]


def sum_of_divisors(n):
    return sum(divisors(n))
