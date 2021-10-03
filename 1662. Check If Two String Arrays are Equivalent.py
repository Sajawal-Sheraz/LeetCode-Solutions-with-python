#https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/






class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        s1 = ''
        s2 = ''
        for x in range(len(word1)):
            s1 = s1 + word1[x]
        for x in range(len(word2)):
            s2 = s2 + word2[x]
        if s1 == s2:
            return True
        else:
            return False
