class Fraction:

    def reduction(a, b):
        max_v = max(a, b)
        lst = [x for x in range(2, max_v) if a % x == 0 and b % x == 0]
        num = [a / x for x in lst if a % x == 0 and b % x == 0]
        denum = [b / x for x in lst if a % x == 0 and b % x == 0]
        if len(num) > 0 and len(denum) > 0:
            m_num = min(num)
            m_denum = min(denum)
        else:
            m_num = a
            m_denum = b
        if m_num == 2 and m_denum == 2:
            return (1, 1)
        return (int(m_num), int(m_denum))

    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        return "{} / {}".format(self.numerator, self.denominator)

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        a = Fraction.reduction(self.numerator, self.denominator)
        b = Fraction.reduction(other.numerator, other.denominator)
        if a[0] == b[0] and a[1] == b[1]:
            return int(a[0] / a[1] + b[0] / b[1])
        return Fraction(a[0] * b[1] + a[1] * b[0], a[1] * b[1])

    def __eq__(self, other):
        a = Fraction.reduction(self.numerator, self.denominator)
        b = Fraction.reduction(other.numerator, other.denominator)
        return a == b

    def __sub__(self, other):
        a = Fraction.reduction(self.numerator, self.denominator)
        b = Fraction.reduction(other.numerator, other.denominator)
        if a[0] == b[0] and a[1] == b[1]:
            return int(a[0] / a[1] - b[0] / b[1])
        return Fraction(a[0] * b[1] - a[1] * b[0], a[1] * b[1])

    def __mul__(self, other):
        a = Fraction.reduction(self.numerator, self.denominator)
        b = Fraction.reduction(other.numerator, other.denominator)
        result = Fraction.reduction(a[0] * b[0], a[1] * b[1])
        if result[0] == result[0] and result[1] == b[1]:
            return int(a[0] / a[1] + b[0] / b[1])
        return Fraction(result[0], result[1])


def main():
    a = Fraction(1, 2)
    b = Fraction(2, 4)
    print(a == b)  # True
    print(a + b)  # 1
    print(a - b)  # 0
    print(a * b)  # 1 / 4'''

if __name__ == '__main__':
    main()
