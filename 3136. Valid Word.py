def isValid(word) -> bool:
    word = word.lower()
    nums = "0123456789"
    vowel = "aeiou"
    consonants = "bcdfghjklmnpqrstvwxyz"
    letters = "abcdefghijklmnopqrstuvwxyz"
    ban_char = "@#$"
    found_vowel = False
    found_con = False
    if len(word) < 4:
        return False
    for i in word:
        print(i)
        input()
        if i in ban_char:
            return False
        if i not in nums and i not in letters:
            return False
        if i in vowel:
            found_vowel = True
        if i in consonants:
            found_con = True

    if found_vowel and found_con:
        return True
    else:
        return False


word = "aya"
print(isValid(word))
