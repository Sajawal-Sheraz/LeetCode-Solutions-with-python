def bubble_sort(numbers):
    total_numbers = len(numbers)

    for num in range(total_numbers):
        for val in range(total_numbers - num - 1):
            if numbers[val] > numbers[val + 1]:
                temp = numbers[val + 1]
                numbers[val + 1] = numbers[val]
                numbers[val] = temp

    return numbers


l = [7, 22, 14, 3, 9, 18, 11, 25, 6, 17]


print(bubble_sort(l))


# Complexity Type	   Complexity
# Time Complexity	   Best: O(n), Average: O(n^2), Worst: O(n^2)
# Space Complexity	    Worst: O(1)
