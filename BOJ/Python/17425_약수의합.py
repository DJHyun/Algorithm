# baekjoon source = "https://www.acmicpc.net/problem/17425"

import sys

sys.stdin = open('input.txt', 'r')

arr = [0] * 1000001
for i in range(1, 1000001):
    for j in range(1, 1000000 // i + 1):
        arr[i * j] += j
for i in range(1, 1000000):
    arr[i + 1] += arr[i]

t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())

    sys.stdout.write(str(arr[n]) + "\n")
