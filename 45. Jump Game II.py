def jump(nums):
    if len(nums) <= 1:
        return 0
    jump = 0
    num = 0
    while num < len(nums):
        if num > 0 and num == len(nums) - 2:
            return jump
        jump += 1
        num = num + nums[num] - 1

    return -1


nums = [1, 2]


print(jump(nums))
