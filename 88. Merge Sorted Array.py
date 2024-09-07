def merge(nums1, m, nums2, n):
    count = 0
    for i in range(m, m + n):
        nums1[i] = nums2[count]
        count += 1
    for i in range(m + n):
        for j in range(i, m + n):

            if nums1[j] < nums1[i]:
                temp = nums1[i]
                nums1[i] = nums1[j]
                nums1[j] = temp

    return nums1


nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


print(merge(nums1, m, nums2, n))
