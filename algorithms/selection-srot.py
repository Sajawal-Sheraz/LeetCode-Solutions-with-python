def selection_sort(arr):
    for index in range(len(arr)):
        target_index = index
        for idx in range(index, len(arr)):
            if arr[idx] < arr[target_index]:
                target_index = idx
        arr[index], arr[target_index] = arr[target_index], arr[index]
    return arr


arr = [64, 25, 12, 22, 11]
selection_sort(arr)
print("Sorted array is:", arr)


# Time Complexity:

# Best Case: O(n^2)
# Average Case: O(n^2)
# Worst Case: O(n^2)


# Space Complexity: O(1)
