with open("/mnt/d/Workspace/Python/ROSALIND-DSA/problem19data.txt", "r") as file:
    n = int(file.readline())

print_count = 0

path = []
used = [False] * (n + 1)


def backtrack():

    if len(path) == n:
        print(*path)
        return

    for num in range(1, n + 1):

        if used[num] == False:

            used[num] = True
            path.append(num)

            backtrack()

            path.pop()
            used[num] = False


def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(n))
backtrack()