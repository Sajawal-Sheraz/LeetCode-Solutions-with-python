def insertion_sort(array):

    for index in range(1, len(array)):
        value = array[index]
        i = index - 1

        while i >= 0 and value < array[i]:
            array[i + 1] = array[i]
            i -= 1
        array[i + 1] = value

    return array


random_list = [14, 46, 43, 27, 57, 41, 45, 21, 70]


print(insertion_sort(random_list))


# Time Complexity:
# Best Case: O(N)
# Average Case: O(N2)
# Worst Case: O(N2).


# Space Complexity: O(1)
