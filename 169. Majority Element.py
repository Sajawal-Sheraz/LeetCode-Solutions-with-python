def majorityElement(nums):
    res = {}
    for i in range(len(nums)):
        res[nums[i]] = res.get(nums[i], 0) + 1
    return max(res, key=res.get)
    # for i in range(len(nums)):
    #     if nums.count(nums[i]) > len(nums)/2:
    #         return nums[i]
    # return 0


nums = [3, 2, 3]
print(majorityElement(nums))
