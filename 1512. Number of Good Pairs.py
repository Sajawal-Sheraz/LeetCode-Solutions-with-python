# Problem Link ===> https://leetcode.com/problems/number-of-good-pairs/


# Good for basic logic
def numIdenticalPairs(nums):
    nums_len = len(nums)
    if nums_len == 0:
        return 0
    count = 0
    for i in range(nums_len - 1):
        for j in range(i + 1, nums_len):
            if nums[i] == nums[j]:
                print(nums[i], "===")
                count += 1
    return count


# Efficient Solution
def numIdenticalPairs(nums):
    count = {}
    result = 0
    for num in nums:
        if num in count:
            result += count[num]
            count[num] += 1
        else:
            count[num] = 1
    return result


print(numIdenticalPairs([1, 2, 3]))
