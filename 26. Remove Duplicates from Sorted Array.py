def removeDuplicates(nums):
    if len(nums) < 2:
        return 1
    j = 0
    while j < len(nums):
        if nums[j] == "_":
            break
        if nums[j + 1] == nums[j]:
            nums.pop(j)
            nums.append("_")
            continue
        j = j + 1
    res = 0
    for i in nums:
        if i == "_":
            continue
        res += 1
    return res

    # Copied effective solution
    # if not nums:
    #     return 0
    # res = 1
    # for i in range(1, len(nums)):
    #     if nums[i] != nums[i - 1]:
    #         nums[res] = nums[i]
    #         res += 1
    # return res


nums = [1, 1, 2, 3, 4, 4, 4, 4, 5]

print(removeDuplicates(nums))
