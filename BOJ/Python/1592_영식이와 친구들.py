# baekjoon source = "https://www.acmicpc.net/problem/1592"

import sys

n, m, l = map(int, sys.stdin.readline().split())
score = [0] * n

score[0] = 1
index = 0
cnt = 0
while True:
    if score[index] % 2:
        index += l
        index %= n
    else:
        index -= l
        index %= n
    score[index] += 1
    cnt += 1
    if score[index] == m:
        print(cnt)
        break
