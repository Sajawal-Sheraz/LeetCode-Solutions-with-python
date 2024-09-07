def binary_search(arr, key):
    arr.sort()
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] < key:
            left = mid + 1
        else:
            right = mid - 1

    return -1


arr = [4, 2, 8, 1, 5, 9, 3]
key = 8


print(binary_search(arr, key))


# Time Complexity:
# Best Case: O(1)
# Average Case: O(log n)
# Worst Case: O(log n)

# Space Complexity: O(1)
