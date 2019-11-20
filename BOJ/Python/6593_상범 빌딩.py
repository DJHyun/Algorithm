# baekjoon source = "https://www.acmicpc.net/problem/6593"

import sys

while True:
    l, r, c = map(int, sys.stdin.readline().split())
    if l == 0 and r == 0 and c == 0:
        break
    arr = [[] for _ in range(l)]
    st, end = ['','',''],['','','']
    for i in range(l):
        for j in range(r + 1):
            if j == r:
                sys.stdin.readline()
                break
            arr[i].append(list(sys.stdin.readline().strip()))
            for a in range(c):
                if arr[i][j][a] == 'S':
                    st[0] = i
                    st[1] = j
                    st[2] = a
                elif arr[i][j][a] == 'E':
                    end[0] = i
                    end[1] = j
                    end[2] = a

    for i in arr:
        for j in i:
            print(j)
        print()

    print(st,end)

