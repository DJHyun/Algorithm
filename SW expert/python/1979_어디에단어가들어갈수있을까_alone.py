# SW Expert Academy
import sys

sys.stdin = open('input (20).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[0] * n for _ in range(n)]
    result = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1 and not visited[i][j]:
                cnt = 0
                visited[i][j] = 1
                for x in range(j, n):
                    visited[i][x] = 1
                    cnt += 1
                    if arr[i][x] == 0:
                        if cnt == k+1:
                            result += 1
                        break
                    if cnt == k and x == n - 1:
                        result += 1

    visited = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[j][i] == 1 and not visited[j][i]:
                cnt = 0
                visited[j][i] = 1
                for x in range(j, n):
                    visited[x][i] = 1
                    cnt += 1
                    if arr[x][i] == 0:
                        if cnt == k+1:
                            result += 1
                        break
                    if cnt == k and x == n - 1:
                        result += 1

    print(f'#{test_case} {result}')
