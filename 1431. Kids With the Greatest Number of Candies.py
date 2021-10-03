# https://leetcode.com/problems/kids-with-the-greatest-number-of-candies/





class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        mx = max(candies)
        for candie in candies:
            if candie + extraCandies >= mx:
                res.append(True)
            else:
                res.append(False)
        return res
