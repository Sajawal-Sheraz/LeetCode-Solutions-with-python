def numberOfSpecialChars(word: str) -> int:
    word = word.lower()
    word_list = list(word)
    word_set = set(word_list)

    return len(word_list) - len(word_set)


word = "aaAbcBC"
print(numberOfSpecialChars(word))
