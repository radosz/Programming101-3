def sum_of_digits(n):
    digits = str(n)
    sum = 0
    for i in digits:
        i = int(i)
        sum += i
    return sum
