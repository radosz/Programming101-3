def palindrome(obj):
    return str(obj) == reverse_obj(obj)


def reverse_obj(obj):
    str_org = str(obj)
    return str_org[::-1]  # list slicing
