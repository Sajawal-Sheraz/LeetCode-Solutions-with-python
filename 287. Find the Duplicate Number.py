def findDuplicate(nums):
    checked = set()
    for i in nums:
        if i in checked:
            return i
        checked.add(i)


nums = [1, 3, 4, 2, 2]

print(findDuplicate(nums))
