def minMaxSum(arr):
    # Write your code here
    min_value = min(arr)
    max_value = max(arr)
    min_index = arr.index(min_value)
    max_index = arr.index(max_value)
    min_arr = list(arr)
    max_arr = list(arr)
    min_arr.pop(min_index)
    max_arr.pop(max_index)
    print(sum(max_arr), sum(min_arr))


arr = [1, 3, 5, 7, 9]
minMaxSum(arr)
