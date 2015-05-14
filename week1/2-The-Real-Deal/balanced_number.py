def len_int(n):
    return len(str(n))


def number_to_list(n):
    result = []
    exp = len_int(n) - 1
    while exp != -1:
        result.append(n // 10**exp)
        n = n - 10**exp * result[-1]
        exp -= 1
    return result


def is_number_balanced(n):

    if n < 9:
        return True
    right = number_to_list(n)
    left = number_to_list(n)

    if len_int(n) % 2 == 0:
        center = len_int(n) // 2
        right = right[center:]
    else:
        center = (len_int(n) // 2) + 1
        right = right[center - 1:]

    left = left[:center]

    print(left)
    print(right)

    return sum(left) == sum(right)
