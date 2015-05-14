def to_digits(n):
    n = str(n)
    answ = []
    digit = 0
    for numb in n:
        digit = int(numb)
        answ.append(digit)
    return answ
