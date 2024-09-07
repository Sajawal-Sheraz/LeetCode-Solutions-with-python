def lexicalOrder(n):
    result = []

    def dfs(num):
        if num > n:
            return
        result.append(num)
        for i in range(10):
            if 10 * num + i <= n:
                dfs(10 * num + i)

    for num in range(1, 10):
        dfs(num)

    return result


n = 13

print(lexicalOrder(n))
