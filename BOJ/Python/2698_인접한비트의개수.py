# baekjoon source = "https://www.acmicpc.net/problem/2698"

import sys

# def backtracking(a,k,check):
#     global N
#     c = [0] * 2
#
#     if k == N-1:
#         print(a)
#     else:
#         k += 1
#         candi = ncandi(a,k,check,c)
#         for i in range(candi):
#             a[k] = c[i]
#             backtracking(a,k,check)
#
# def ncandi(a,k,check,c):
#
#     ncandi = 0
#     for i in range(2):
#         c[ncandi] = i
#         ncandi += 1
#
#     return ncandi


T = int(sys.stdin.readline())

for _ in range(T):
    N,K = map(int,sys.stdin.readline().split())
    print(N,K)
    a = [-1]*N

    # backtracking(a,-1,K)







    