s = "pwwkew"


def result(s):
    seen = {}
    l = 0
    length = 0
    for i in range(len(s)):
        char = s[i]
        if char in seen and seen[char] >= l:
            l = seen[char] + 1
        else:
            length = max(length, i - l + 1)
        seen[char] = i

    return length


print(result(s))
# pw wke w
# abc abcab
# bbbb
