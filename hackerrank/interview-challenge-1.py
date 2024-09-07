def plusMinus(arr):
    # Write your code here
    unique_arr = {
        "p": 0,
        "n": 0,
        "z": 0,
    }
    len_arr = len(arr)
    for i in arr:
        if i == 0:
            unique_arr["z"] = 1 + unique_arr.get("z")
        elif i >= 1:
            unique_arr["p"] = 1 + unique_arr.get("p")
        else:
            unique_arr["n"] = 1 + unique_arr.get("n")
    for i, v in unique_arr.items():
        print(f"{float(v / len_arr):.6f}")


arr = [-4, 3, -9, 0, 4, 1]
plusMinus(arr)
