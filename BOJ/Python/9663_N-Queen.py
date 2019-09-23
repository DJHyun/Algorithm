# baekjoon source = "https://www.acmicpc.net/problem/9663"

import sys

def backtracking(a,k,n):
    global cnt
    c = [0] * n

    if k == n:
        cnt += 1
    else:
        k += 1
        ncandi = construct(a, k, n, c)
        for i in range(ncandi):
            a[k] = c[i]
            backtracking(a, k, n)

def construct(a,k,n,c):
    check = [False] * n

    for i in range(1,k):
        check[a[i]] = True
        if a[i] + (k-i) < N:
            check[a[i]+(k-i)] = True
        if a[i] - (k-i) >= 0:
            check[a[i]-(k-i)] = True

    ncandi = 0

    for i in range(0,n):
        if check[i] == False:
            c[ncandi] = i
            ncandi += 1
    
    return ncandi
    
N = int(sys.stdin.readline())
a = [0] * (N+1)
ncandi = N
cnt = 0

backtracking(a, 0, N)
print(cnt)