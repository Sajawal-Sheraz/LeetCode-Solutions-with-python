def findTheWinner(n, k):
    people = list(range(1, n + 1))
    pos = 0
    k = k - 1
    while len(people) > 1:
        pos = (pos + k) % len(people)
        people.pop(pos)
    return people[0]


123
n = 5
k = 2
print(findTheWinner(n, k))
