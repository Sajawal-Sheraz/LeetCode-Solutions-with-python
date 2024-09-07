def linear_search(arr, key):
    for index in range(len(arr)):
        if arr[index] == key:
            return index

    return -1


arr = [4, 2, 8, 1, 5, 9, 3]
print(linear_search(arr, 8))
