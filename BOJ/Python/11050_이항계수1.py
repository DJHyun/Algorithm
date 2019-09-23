# baekjoon source = "https://www.acmicpc.net/problem/1003"
import sys

N, K = map(int, sys.stdin.readline().split())

K = min(K, N - K)
re_n = 1
re_k = 1
for i in range(K,0,-1):
    re_n *= N
    N -= 1

    re_k *= i

print((re_n//re_k))

