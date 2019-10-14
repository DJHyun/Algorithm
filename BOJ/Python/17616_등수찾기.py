# baekjoon source = "https://www.acmicpc.net/problem/17616"

import sys
from collections import deque

def solution(x):
    global result, back_result
    q = deque()
    q.append(x)
    while q:
        t = q.popleft()
        for i in range(len(arr[t])):
            if arr[t][i] > 0 and not visited[arr[t][i]]:
                result += 1
                visited[arr[t][i]] = 1
                q.append(arr[t][i])

    q.append(x)
    while q:
        t = abs(q.popleft())
        for i in range(len(arr[t])):
            if arr[t][i] < 0 and not two_visited[abs(arr[t][i])]:
                back_result += 1
                two_visited[abs(arr[t][i])] = 1
                q.append(arr[t][i])

n, m, x = map(int, sys.stdin.readline().split())
arr = deque([[] for _ in range(n + 1)])
back = deque([[] for _ in range(n + 1)])
visited = [0] * (n + 1)
two_visited = [0]*(n+1)
back_result = 0
result = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    arr[a].append(b)
    arr[b].append(-a)
visited[x] = 1
solution(x)
sys.stdout.write(str(back_result+1)+" ")
sys.stdout.write(str(n-result))
