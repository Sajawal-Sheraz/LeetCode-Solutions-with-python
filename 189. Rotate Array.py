def rotate(nums, k):
    nums[: k + 1]
    nums[k + 1 :].reverse()
    print(k_split_prev)

    return k_split_nxt + k_split_prev

    # for i in range(k):
    #     temp = nums[-1]
    #     for j in range(len(nums) - 1, 0, -1):
    #         nums[j] = nums[j - 1]
    #     nums[0] = temp


nums = [1, 2, 3, 4, 5, 6, 7]
k = 3

print(rotate(nums, k))
[5, 6, 7, 1, 2, 3, 4]
