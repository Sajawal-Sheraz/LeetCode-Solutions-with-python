#https://leetcode.com/problems/build-array-from-permutation/


class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        ans = []
        for num in range(len(nums)):
            ans.append(nums[nums[num]])
        return ans
            
