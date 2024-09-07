# Problem Link ===> https://leetcode.com/problems/jewels-and-stones/description/


def smallerNumbersThanCurrent(nums):
    result = []
    for i in nums:
        count = 0
        for j in nums:
            if i == j:
                continue
            elif j < i:
                count += 1
        result.append(count)

    return result


nums = [8, 1, 2, 2, 3]
print(smallerNumbersThanCurrent(nums))
