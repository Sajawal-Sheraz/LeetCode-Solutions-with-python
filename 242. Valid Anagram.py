def isAnagram(s, t):
    if len(s) != len(t):
        return False
    s_dict = {}
    t_dict = {}

    for i in range(len(s)):
        s_dict[s[i]] = s_dict.get(s[i], 0) + 1
        t_dict[t[i]] = t_dict.get(t[i], 0) + 1
    if len(s_dict) != len(t_dict):
        return False

    for i in range(len(s)):

        if s_dict.get(s[i], 0) != t_dict.get(s[i], -1):
            return False
    return True


s = "xaaddy"
t = "xbbccy"

print(isAnagram(s, t))
