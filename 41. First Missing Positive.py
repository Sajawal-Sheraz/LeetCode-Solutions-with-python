def firstMissingPositive(nums):
    nums.sort()
    count = 1
    for num in nums:
        if num == count:
            count += 1
        elif num > count:
            return count
    return count


nums = [3, 4, -1, 1]
print(firstMissingPositive(nums))
