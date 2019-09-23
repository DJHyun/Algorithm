# baekjoon source = "https://www.acmicpc.net/problem/5063"
import sys

N = int(sys.stdin.readline())

for _ in range(N):
    a, b, c = map(int, sys.stdin.readline().split())
    if a > (b - c):
        print("do not advertise")
    elif a == (b - c):
        print("does not matter")
    else:
        print("advertise")
