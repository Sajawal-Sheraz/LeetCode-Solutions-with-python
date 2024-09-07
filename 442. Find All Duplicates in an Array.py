# Example 1:

# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [2,3]
# Example 2:

# Input: nums = [1,1,2]
# Output: [1]
# Example 3:

# Input: nums = [1]
# Output: []


def findDuplicates(nums):
    seen = set()
    duplicates = set()

    for i in nums:
        if i in seen:
            duplicates.add(i)
        else:
            seen.add(i)
    return list(duplicates)


nums = [1]
print(findDuplicates(nums))
