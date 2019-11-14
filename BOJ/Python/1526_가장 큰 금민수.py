# baekjoon source = "https://www.acmicpc.net/problem/1526"

import sys

n = int(sys.stdin.readline())

for i in range(n,3,-1):

    st = str(i)

    for j in range(len(st)):
        if st[j] != '4' and st[j] != '7':
            break
    else:
        print(i)
        break

