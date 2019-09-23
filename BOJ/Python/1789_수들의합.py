# baekjoon source = "https://www.acmicpc.net/problem/1789"
import sys

S = int(sys.stdin.readline())

idx = 1
while True:
    if S <= 0:
        break

    if S - idx < idx + 1:
        break

    S -= idx
    idx += 1

print(idx)