import pprint
from copy import deepcopy
from numbers_in_matrix import sum_matrix


def down(m, element_tuple):
    row = element_tuple[0]
    column = element_tuple[1]
    row += 1
    if row < 0 or column < 0 or row > len(m) - 1 or column > len(m) - 1:
        return 0

    return(row, column)


def up(m, element_tuple):
    row = element_tuple[0]
    column = element_tuple[1]
    row -= 1

    if row < 0 or column < 0 or row > len(m) - 1 or column > len(m) - 1:
        return 0
    return(row, column)


def left(m, element_tuple):
    row = element_tuple[0]
    column = element_tuple[1]
    column -= 1
    if row < 0 or column < 0 or row > len(m) - 1 or column > len(m) - 1:
        return 0
    return(row, column)


def right(m, element_tuple):
    row = element_tuple[0]
    column = element_tuple[1]
    column += 1
    if row < 0 or column < 0 or row > len(m) - 1 or column > len(m) - 1:
        return 0
    return(row, column)


def diag_p1(m, element_tuple):

    row = element_tuple[0]
    column = element_tuple[1]
    row += 1
    column += 1

    if row < 0 or column < 0 or row > len(m) - 1 or column > len(m) - 1:
        return 0
    return(row, column)


def diag_p2(m, element_tuple):
    row = element_tuple[0]
    column = element_tuple[1]
    row += 1
    column -= 1
    if row < 0 or column < 0 or row > len(m) - 1 or column > len(m) - 1:
        return 0
    return(row, column)


def diag_p3(m, element_tuple):
    row = element_tuple[0]
    column = element_tuple[1]
    row -= 1
    column += 1
    if row < 0 or column < 0 or row > len(m) - 1 or column > len(m) - 1:
        return 0
    return(row, column)


def diag_p4(m, element_tuple):
    row = element_tuple[0]
    column = element_tuple[1]
    row -= 1
    column -= 1
    if row < 0 or column < 0 or row > len(m) - 1 or column > len(m) - 1:
        return 0
    return(row, column)


def neighbors(m, t):
    return [up(m, t), down(m, t), left(m, t), right(m, t), diag_p1(m, t), diag_p2(m, t), diag_p3(m, t), diag_p4(m, t)]


def init_keys(m):
    element_tuple = []
    for row in range(len(m)):
        for column in range(len(m[row])):
            element_tuple.append((row, column))
    return element_tuple


def matrix_bombing_plan(m):
    old_m = deepcopy(m)
    keys = init_keys(m)
    all_n = {k: neighbors(m, k) for k in keys}
    result = {}

    for k in keys:
        for e in all_n[k]:
            if isinstance(e, tuple):
                if m[e[0]][e[1]] - m[k[0]][k[1]] < 0:
                    m[e[0]][e[1]] = 0
                else:
                    m[e[0]][e[1]] = m[e[0]][e[1]] - m[k[0]][k[1]]
        result[k] = sum_matrix(m)
        m = deepcopy(old_m)
    return result


def print_matrix(m):
    pr = "\n".join(str(m) for m in m)
    pr = pr.replace(",", "")
    pr = pr.replace("[", "")
    pr = pr.replace("]", "")
    print(pr)


def main():
    m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result = matrix_bombing_plan(m)

    pp = pprint.PrettyPrinter()
    pp.pprint(result)

if __name__ == '__main__':
    main()
