def removeDuplicates(nums):
    nums_len = len(nums)
    if nums_len < 2:
        return nums_len
    nxt = 2
    prev = 1
    curr = 0
    c = 0
    for i in range(nums_len - 2):
        if nums[nxt] == nums[prev] and nums[prev] == nums[curr]:
            nums.pop(curr)
            nums.append("_")
            c += 1
            continue
        nxt += 1
        prev += 1
        curr += 1
    res = nums_len - c
    return res


nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]


print(removeDuplicates(nums))
