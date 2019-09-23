# baekjoon source = "https://www.acmicpc.net/problem/5576"

import sys
a,b = [], []
for i in range(10):
    a.append(int(sys.stdin.readline()))
for i in range(10):
    b.append(int(sys.stdin.readline()))
a.sort();b.sort()
print(sum(a[7:]),sum(b[7:]))