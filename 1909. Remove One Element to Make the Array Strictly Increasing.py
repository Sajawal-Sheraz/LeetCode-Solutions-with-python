# https://leetcode.com/problems/remove-one-element-to-make-the-array-strictly-increasing/description/

removed_once = False


def canBeIncreasing(nums):
    count = 0          
    for i in range(len(nums)):          
        valid = True
        last = 0
        for j in range(len(nums)):                  
            if j == i:   
                continue
            if nums[j] <= last:   
                valid = False
                break
            last = nums[j]      
        if valid:
            count += 1

    return count != 0


nums = [
    [1, 2, 10, 5, 7],  # True
    [2, 3, 1, 2],  # false
    [105, 924, 32, 968],  # True
    [1, 1, 1],  # false
]

for i in nums:
    print(canBeIncreasing(i))
