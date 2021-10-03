#https://leetcode.com/problems/final-value-of-variable-after-performing-operations/




class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        r = 0
        for x in operations:
            if x == 'X++' or x =='++X':
                r=r+1
            elif x == 'X--' or x =='--X':
                r=r-1
                
        return r
