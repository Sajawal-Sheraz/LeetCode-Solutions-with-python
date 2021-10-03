#https://leetcode.com/problems/richest-customer-wealth/






class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        res = []
        sum = 0
        for x in accounts:
            for r in x:
                sum = sum + int(r)
            res.append(sum)
            sum = 0
        return max(res)
