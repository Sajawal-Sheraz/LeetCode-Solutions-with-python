def lengthOfLastWord(s):
    s = s.split()
    return len(s[-1])


s = "   fly me   to   the moon  "

print(lengthOfLastWord(s))
