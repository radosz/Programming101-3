from balanced_number import number_to_list
#zero_insertion

def zero_insert(n):
    list_n = number_to_list(n)
    result = []
    missing_n = []
    size = len(list_n)

    for i in range(size):
        print("{0} - {1}".format(i, i + 1))
        if (i + 1 < size):
            if list_n[i] == list_n[i + 1] or (list_n[i] + list_n[i + 1]) % 10 == 0:
                result.append(list_n[i])
                result.append(0)

    if result[-1] == 0:
        result.append(list_n[size - 1])

    missing_n = [x for x in list_n if not x in result]
    result += missing_n
    return to_number(result)


def to_number(digits):
    digits = [str(x) for x in digits]
    number = "".join(digits)
    number = int(number)
    return number
