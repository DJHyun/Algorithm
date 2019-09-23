# baekjoon source = "https://www.acmicpc.net/problem/14501"

def bfs(a, sum_):
    global n

    check = 0
    q = [[a, sum_]]
    while q:
        t = q.pop(0)
        check = max(check, t[1])
        for i in range(t[0], n):
            if i > t[0] + arr[t[0]][0] - 1 and i + arr[i][0] < n + 1:
                q.append([i, t[1] + arr[i][1]])
    return check

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    if i + arr[i][0] < n+1:
        result = max(result, bfs(i, arr[i][1]))
print(result)
