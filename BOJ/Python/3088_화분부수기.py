# baekjoon source = "https://www.acmicpc.net/problem/3088"

'''
5
3 4 1
2 5 6
7 2 8
2 1 9
11 10 9
'''

import sys

n = int(sys.stdin.readline())
r = 0
d = [0] * 1000001
for _ in range(n):
    flag = True
    a, b, c = map(int, sys.stdin.readline().split())
    if d[a] == 1:
        d[b] = d[c] = 1
        flag = False
        break
    if d[b] == 1:
        d[a] = d[c] = 1
        flag = False
        break
    if d[c] == 1:
        d[a] = d[b] = 1
        flag = False
        break

    if flag:
        d[a] = d[b] = d[c] = 1
        r += 1
sys.stdout.write(str(r))
