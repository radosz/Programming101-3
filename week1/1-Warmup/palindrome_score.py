from palindrome import reverse_obj
from palindrome import palindrome as is_palindrome


def p_score(n):
    score = 1
    if is_palindrome(n):
        return score
    else:
        while is_palindrome(n) == False:
            score += 1
            n = int(reverse_obj(n)) + n
    return score
