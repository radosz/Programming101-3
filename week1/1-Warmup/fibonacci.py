def nth_fibonacci(n):
    result = []
    a, b = 0, 1
    while len(result) != n:
        result.append(b)
        a, b = b, a + b
    return result
