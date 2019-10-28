# baekjoon source = "https://www.acmicpc.net/problem/1707"

import sys

t = int(sys.stdin.readline())
for tc in range(t):
    v, e = map(int, sys.stdin.readline().split())
    visited = [0] * (v + 1)
    result = 0
    flag = True

    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        if i == 0:
            visited[a] = 1
            visited[b] = 2
            continue

        if not visited[a]:
            if not visited[b]:
                visited[a] = 1
                visited[b] = 2
            elif visited[b] == 1:
                visited[a] = 2
            else:
                visited[a] = 1
        elif visited[a] == 1:
            if not visited[b]:
                visited[b] = 2
            elif visited[b] == 1:
                flag = False
        else:
            if not visited[b]:
                visited[b] = 1
            elif visited[b] == 2:
                flag = False

    if flag:
        print('YES')
    else:
        print('NO')
