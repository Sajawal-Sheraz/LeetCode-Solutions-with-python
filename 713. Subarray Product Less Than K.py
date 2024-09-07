def numSubArrayProductLessThanK(nums, k):
    if k <= 1:
        return 0

    product = 1
    count = left = 0

    for right, num in enumerate(nums):
        product *= num
        while product >= k:
            product /= nums[left]
            print(product)

            left += 1
        count += right - left + 1

    return count


nums = [10, 5, 2, 6]
k = 100
print(numSubArrayProductLessThanK(nums, k))
