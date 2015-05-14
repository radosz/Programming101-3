def count_vowels(str):
    vowels_l = "aeiouy"
    vowels_c = vowels_l.upper()
    count = 0
    for i in str:
        if i in vowels_l:
            count += 1
        elif i in vowels_c:
            count += 1
    return count
