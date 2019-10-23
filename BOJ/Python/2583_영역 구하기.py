# baekjoon source = "https://www.acmicpc.net/problem/2583"

import sys

m,n,k = map(int,sys.stdin.readline().split())
arr = [[0]*(n*2+1) for _ in range(m*2+1)]

for i in arr:
    print(i)
print()

for i in range(k):
    j = list(map(int,sys.stdin.readline().split()))

for i in arr:
    print(i)
print()
