import sys

sys.stdin = open("5251_최소이동거리.txt", "r")

def bfs(x):
    global m, result

    q = []
    q.append([x, 0])
    while q:
        t = q.pop()
        for i in range(len(arr[t[0]])):
            if arr[t[0]][i]:
                if i == n:
                    result = min(result, t[1] + arr[t[0]][i])
                elif result <= t[1] + arr[t[0]][i]:
                    continue
                else:
                    q.append([i, t[1] + arr[t[0]][i]])


    print(f'#{test_case} {result}')

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [[0] * (n + 1) for _ in range(n + 1)]
    visited = [0] * (n + 1)
    result = 9999999999

    for i in range(m):
        num = list(map(int, input().split()))
        arr[num[0]][num[1]] = num[2]

    bfs(0)
