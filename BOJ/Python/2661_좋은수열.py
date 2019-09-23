# baekjoon source = "https://www.acmicpc.net/problem/2661"

import sys

def backtracking(a,k,b):
    global flag
    c = [0] * 4
    if flag:
        if k == b:
            print(''.join(map(str,a[1:])))
            flag = False
        else:
            k += 1
            candi = ncandi(a,k,b,c)
            for i in range(candi):
                a[k] = c[i]
                backtracking(a,k,b)

def ncandi(a,k,b,c):
    check = [0] * 4

    check[a[k-1]] = 1
    
    j = 1
    for i in range(3,k,2):
        if a[k-i:k-i+j] == a[k-j:k]:
            check[a[k-i+j]] = 1
        j += 1

    candi = 0
    
    for i in range(1,4):
        if not check[i]:
            c[candi] = i
            candi += 1

    return candi

N = int(sys.stdin.readline())
a = [0]*(N+1)
flag = True

backtracking(a,0,N)

