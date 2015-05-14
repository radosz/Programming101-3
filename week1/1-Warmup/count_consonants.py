from count_vowels import count_vowels


def count_consonants(str):

    del_char = [chr(x) for x in range(32, 65)]
    del_char += [chr(x) for x in range(91, 97)]
    # ASCII table http://www.bibase.com/images/ascii.gif
    del_char += [chr(x) for x in range(123, 126)]

    for char in del_char:
        str = str.replace(char, "")

    return len(str) - count_vowels(str)
