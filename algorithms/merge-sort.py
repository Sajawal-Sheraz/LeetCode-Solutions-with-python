def combiner(left, right):

    result = []
    left_index = 0
    right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    if left_index < len(left):
        result.extend(left[left_index:])
    if right_index < len(right):
        result.extend(right[right_index:])

    return result


def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return combiner(left, right)


random_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]


print(merge_sort(random_list))


# Time Complexity:
# Best Case: O(n log n), When the array is already sorted or nearly sorted.
# Average Case: O(n log n), When the array is randomly ordered.
# Worst Case: O(n log n), When the array is sorted in reverse order.


# Space Complexity: O(n)
