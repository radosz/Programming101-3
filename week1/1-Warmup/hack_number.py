from palindrome import palindrome as is_palindrome


def is_odd_one(n):
    str_num = bin_num_to_str(n)
    count_one = [int(x) for x in str_num if x == "1"]
    count_one = len(count_one)
    if count_one % 2 != 0:
        return True
    return False


def bin_num_to_str(n):
    return str(bin(n)).replace("0b", "")


def next_hack(n):
    while True:
        n += 1
        binary = bin_num_to_str(n)
        if is_palindrome(binary) and is_odd_one(n):
            break
    return n
