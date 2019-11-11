# baekjoon source = "https://www.acmicpc.net/problem/17825"

import sys
from collections import deque

one = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 0]
two = [0, 2, 4, 6, 8, 10, 13, 16, 19, 25, 30, 35, 40, 0]
three = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 25, 30, 35, 40, 0]
four = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 28, 27, 26, 25, 30, 35, 40, 0]
check = [0, one[:], two[:], three[:], four[:]]
visited = [0, one[:], two[:], three[:], four[:]]

score = list(map(int, sys.stdin.readline().split()))
result = 0

q = deque()
tq = [[0, 0, 0, 0, 1, 1, 1, 1, 0]]
index = 0
result = float('-inf')

while tq:

    go = score[index]
    print(tq)
    q = deque(tq[:])
    tq.clear()
    while q:
        t = q.popleft()
        la = []
        for c in range(4):
            if t[c] == -1:
                continue
            visited[t[c + 4]][t[c]] = -1
            la.append([t[c+4],t[c]])
            if check[t[c + 4]][t[c]] == 10:
                for a in range(1, 5):
                    b = check[a].index(10)
                    visited[a][b] = -1
                    la.append([a, b])
            elif check[t[c + 4]][t[c]] == 20:
                for a in range(1, 5):
                    if a == 2:
                        continue
                    b = check[a].index(20)
                    visited[a][b] = -1
                    la.append([a, b])
            elif check[t[c + 4]][t[c]] == 30:
                for a in range(1, 5):
                    b = check[a].index(30)
                    visited[a][b] = -1
                    la.append([a, b])

        for mal in range(4):
            new = t[:]
            if new[mal] == - 1:
                continue
            if new[mal] + go < len(visited[new[mal + 4]]) and visited[new[mal + 4]][new[mal] + go] != -1:
                visited[new[mal + 4]][new[mal]] = 0
                new[mal] += go
                if new[mal + 4] == 1:
                    if check[new[mal + 4]][new[mal]] == 10:
                        new[mal + 4] = 2
                    elif check[new[mal + 4]][new[mal]] == 20:
                        new[mal + 4] = 3
                    elif check[new[mal + 4]][new[mal]] == 30:
                        new[mal + 4] = 4
                new[8] += check[new[mal + 4]][new[mal]]
                visited[new[mal + 4]][new[mal]] = -1
                la.append([new[mal + 4], new[mal]])

                if check[new[mal + 4]][new[mal]] == 10:
                    for a in range(1, 5):
                        b = check[a].index(10)
                        visited[a][b] = -1
                        la.append([a,b])
                elif check[new[mal + 4]][new[mal]] == 20:
                    for a in range(1, 5):
                        if a == 2:
                            continue
                        b = check[a].index(20)
                        visited[a][b] = -1
                        la.append([a, b])
                elif check[new[mal + 4]][new[mal]] == 30:
                    for a in range(1, 5):
                        b = check[a].index(30)
                        visited[a][b] = -1
                        la.append([a, b])


                # if result < new[8]:
                #     print(new)
                result = max(result, new[8])
                tq.append(new)
            elif new[mal] + go >= len(visited[new[mal + 4]]):
                new[mal] = -1
                tq.append(new)
        print(la)
        for c in range(len(la)):
            visited[la[c][0]][la[c][1]] = 0

    index += 1
    if index > 9:
        break
print(result)
