# baekjoon source = "https://www.acmicpc.net/problem/2884"
import sys

H,M = map(int,sys.stdin.readline().split())

if M >= 45:
    print(H, M-45)
else:
    H -= 1
    if H < 0:
        H = 23
    M = M + 60
    print(H, M-45)
