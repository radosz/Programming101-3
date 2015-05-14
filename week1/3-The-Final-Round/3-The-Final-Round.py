from datetime import date
from calendar import monthrange

# Count words


def count_words(arr):
    count_dict = {}
    count_word = [arr.count(c) for c in arr]
    i = 0
    for e in arr:
        count_dict[e] = count_word[i]
        i += 1
    return count_dict

# Unique words


def unique_words_count(arr):
    set_w = {x for x in arr}
    word = [x for x in set_w]
    return len(count_words(word))

# NaN Expand


def nan_expand(n):
    if n != 0:
        str_n = "Not a " * n
        str_n += "NaN"
        if n > 1:
            str_n += " "

        if str_n[-1] == " ":
            return str_n[:-1]
        else:
            return str_n

    return ""

# Iterations of NaN Expand


def iterations_of_nan_expand(str_nan):

    if str_nan == "":
        return 0

    if str_nan.count("Not a") != 0:
        if len(nan_expand(str_nan.count("Not a"))) == len(str_nan):
            return str_nan.count("Not a")
        else:
            return False

    return False

# Integer prime factorization


def is_prime(n):
    if n == 1 or n <= 0:
        return False

    divisors = [x for x in range(2, n) if x != n]

    for d in divisors:
        if n % d == 0:
            return False
    return True


def divide_count(n, k):
    times = 0

    while n != 1 and n % k == 0:
        times += 1
        n = n // k

    return times


def next_prime(n):
    n += 1

    while not is_prime(n):
        n += 1

    return n


def prime_factorization(n):
    result = []

    current_prime = 2

    while n != 1:
        times = divide_count(n, current_prime)

        if times != 0:
            result.append((current_prime, times))
            n = n // current_prime ** times

        current_prime = next_prime(current_prime)

    return result

# The group function


def generate_list(items):
    result = []
    for e in items:
        if items[0] == e:
            result.append(e)
        elif items[0] in result:
            break
    return result


def remove_elements(gen_l, items):
    for e in gen_l:
        if e in items:
            items.remove(e)
    return items


def group(items):
    result = []
    while len(items) != 0:
        gen_l = generate_list(items)
        remove_elements(gen_l, items)
        result.append(gen_l)
    return result

# Longest subsequence of equal consecutive elements


def max_consecutive(items):
    group_i = group(items)
    return max([len(x) for x in group_i])

# Group By


def groupby(func, seq):
    result = {}
    for n in seq:
        result[func(n)] = [x for x in seq if func(x) == func(n)]
    return result


# Spam and Eggs


def division_five(number):
    d_list = [x for x in range(5, number + 1) if x % 5 == 0]
    return [number // x for x in d_list if number % x == 0]


def spam_eggs(number):
    d_list = [x for x in range(3, number + 1) if x % 3 == 0]
    d_five = division_five(number)
    d_three = [number // x for x in d_list if number %
               x == 0 and x not in d_five]
    return {"eggs": d_five, "spam": d_three}


def prepare_meal(number):

    eggs = len(spam_eggs(number)["eggs"])
    spam = len(spam_eggs(number)["spam"])

    spam_list = []
    eggs_list = []
    if spam > 0:
        if eggs > 0:
            eggs_list.append("and")
    spam_list += ["spam" for x in range(spam)]

    if eggs > 0:
        eggs_list.append("eggs")

    result = spam_list + eggs_list
    return " ".join(result)

# Reduce file path


def reduce_file_path(path):

    path = path.split("/")
    path = [x for x in path if x != ""]
    path.insert(0, "/")

    while path[-1] == "..":
        path.pop()
        if path[-1] != "/":
            path.pop()

    while path[-1] == ".":
        path.pop()

    if len(path) == 1 and path[0] == "/":
        return "/"

    return "/".join(path)[1:]

#Word from a^nb^n

def is_an_bn(word):
    arr = [c for c in word]
    dict_w = count_words(arr)

    if word == "":
        return True

    try:

        n = dict_w["a"]
        word_n = ["a" for x in range(n)]
        word_n += ["b" for x in range(n)]
        if "".join(word_n) == word:
            return True

    except KeyError:
        return False

    return False

# Goldbach Conjecture


def is_even(n):
    return n % 2 == 0


def prime_numbers(n):
    return [x for x in range(1, n + 1) if is_prime(x)]


def goldbach(n):

    result = []
    skip = []

    if is_even(n) == False or n < 2:
        return False

    p_numbers = prime_numbers(n)

    for n_1 in p_numbers:
        for n_2 in p_numbers:

            if n_1 + n_2 == n and n_1 not in skip:
                result.append((n_1, n_2))
                skip.append(n_2)

    return result

# Credit card validation


def is_valid_count_digit(number):
    return len(str(number)) % 2 != 0


def odd_position_digits(str_number):
    return [int(str_number[i]) for i in range(1, len(str_number), 2)]


def even_position_digits(str_number):
    return [int(str_number[i]) for i in range(0, len(str_number), 2)]


def all_double(list_numbers):
    return [x * 2 for x in list_numbers]


def insert_new_digits(str_number):
    even = even_position_digits(str_number)
    new_digits = all_double(odd_position_digits(str_number))
    range_d = min(len(even), len(new_digits))
    result = []
    for i in range(range_d):
        result.append(even[i])
        result.append(new_digits[i])

    result.append(even[-1])
    result = [str(digit) for digit in result]
    result = "".join(result)
    result = [int(c) for c in result]

    return result


def is_credit_card_valid(number):
    str_number = str(number)
    c1 = is_valid_count_digit(number)
    c2 = sum(insert_new_digits(str_number)) % 10 == 0
    return c1 and c2


# Magic Square


def matrix_col_sum(matrix):
    result = []
    for i in range(len(matrix)):
        result.append(sum([x[0] for x in matrix]))
    return result


def is_all_equals(n):
    for i in range(len(n)):
        if i + 2 > len(n):
            break
        if n[i] == n[i + 1] and n[i] == n[i + 2]:
            return True
    return False


def matrix_diag_sum(matrix):
    result = 0
    i = 0
    for i in range(len(matrix)):
        if i < len(matrix):
            result += matrix[i][i]
            i += 1
        else:
            break
    return result


def matrix_diag_sum2(matrix):
    matrix = [m for m in reversed(matrix)]
    return matrix_diag_sum(matrix)


def magic_square(matrix):
    col_sum = matrix_col_sum(matrix)
    return is_all_equals(col_sum) and col_sum[0] == matrix_diag_sum(matrix) and col_sum[0] == matrix_diag_sum2(matrix)

# Friday Years


def friday_counter(years):
    month = [x for x in range(1, 13)]
    count = 0
    result = []
    for y in years:
        for m in month:
            for d in range(1, monthrange(y, m)[-1] + 1):
                if date(y, m, d).weekday() == 4:
                    count += 1

        result.append(count)
        count = 0
    return result


def friday_years(start, end):
    years = [y for y in range(start, end + 1)]
    return friday_counter(years).count(53)
