import sys

sys.stdin = open('input.txt', 'r')

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

def dfs(a, b, sum_):
    global result

    if not check(a, b):
        return 0

    if a == n - 1 and b == n - 1:
        if result > sum_:
            result = sum_
            visited[a][b] = sum_
        else:
            return 0

    if sum_ >= result:
        return 0

    if sum_ < visited[a][b]:
        visited[a][b] = sum_
    else:
        return 0

    dfs(a + 1, b, sum_ + arr[a][b])
    dfs(a, b + 1, sum_ + arr[a][b])
    dfs(a - 1, b, sum_ + arr[a][b])
    dfs(a, b - 1, sum_ + arr[a][b])

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input())) for _ in range(n)]
    visited = [[float('inf')] * n for _ in range(n)]

    result = float('inf')

    print(n)
    for i in arr:
        print(i)
    print()
    dfs(0, 0, 0)

    for i in visited:
        print(i)
    print()

    print(f'#{test_case} {result}')
