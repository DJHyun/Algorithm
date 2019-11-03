# baekjoon source = "https://www.acmicpc.net/problem/1707"

import sys
from collections import deque

def solution(x):
    global v

    q = deque([x])
    visited = [0] * (v + 1)
    visited[x] = 1

    while q:
        t = q.popleft()
        for i in arr[t]:
            if not visited[i]:
                check[i] = 1
                q.append(i)
                if visited[t] == 1:
                    visited[i] = 2
                else:
                    visited[i] = 1
            else:
                if visited[i] == 1:
                    if visited[t] == 1:
                        return False
                    visited[t] = 2
                elif visited[i] == 2:
                    if visited[t] == 2:
                        return False
                    visited[t] = 1
    return True

t = int(sys.stdin.readline())
for tc in range(t):
    v, e = map(int, sys.stdin.readline().split())
    arr = [deque() for _ in range(v + 1)]
    check = [0]*(v+1)

    for _ in range(e):
        a, b = map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, v + 1):
        if not check[i]:
            check[i] = 1
            if not solution(i):
                print('NO')
                break
    else:
        print('YES')

