# baekjoon source = "https://www.acmicpc.net/problem/1707"

import sys

t = int(sys.stdin.readline())
for tc in range(t):
    v, e = map(int, sys.stdin.readline().split())
    arr = [[] for _ in range(v + 1)]
    visited = [0] * (v + 1)

    for i in range(e):
        a, b = map(int, sys.stdin.readline().split())
        arr[a].append(b)
        arr[b].append(a)

    for i in range(1, v + 1):
        flag = False
        for j in arr[i]:
            if not visited[i]:
                if not visited[j]:
                    visited[i] = 1
                    visited[j] = 2
                elif visited[j] == 1:
                    visited[i] = 2
                elif visited[j] == 2:
                    visited[i] = 1
            elif visited[i] == 1:
                if not visited[j]:
                    visited[j] = 2
                elif visited[j] == 1:
                    flag = True
                    break
            elif visited[j] == 2:
                if not visited[j]:
                    visited[j] = 1
                elif visited[j] == 2:
                    flag = True
                    break

        if flag:
            print('NO')
            break

    else:
        print('YES')
