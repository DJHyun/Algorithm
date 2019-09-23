import sys

sys.stdin = open("5209_최소생산비용.txt", "r")

def solution(arr, k, min_sum):
    global result
    k += 1

    if min_sum >= result:
        return

    if k == n:
        result = min(result, min_sum)

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            solution(arr, k, min_sum + arr[k][i])
            visited[i] = 0

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    result = 999999

    solution(arr, -1, 0)
    print(f'#{test_case} {result}')