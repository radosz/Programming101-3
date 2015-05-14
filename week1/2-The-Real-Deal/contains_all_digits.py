def contains_digits(number, digits):
    lst_number = [int(x) for x in str(number)]
    bool_lst = []
    for i in lst_number:
        for y in digits:
            if i == y:
                bool_lst.append(1)
            else:
                bool_lst.append(0)
    if 0 in bool_lst:
        return False
    return True
