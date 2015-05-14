def char_histogram(string):

    dict_hist_c = {}
    checked_char = []

    for i in range(len(string)):
        count = 0
        for y in range(len(string)):
            if string[i] == string[y] and string[i] not in checked_char:
                count += 1
                dict_hist_c[string[i]] = count
        checked_char.append(string[i])
    return sort_result(string, dict_hist_c)


def sort_result(string, dict_hist_c):
    answ = "{ "
    for ch in string:
        if ch not in answ:
            answ += "'{0}': {1} ,".format(ch, dict_hist_c[ch])

    answ = answ[:-1]  # remove last ","
    answ += "}"

    print(answ)
