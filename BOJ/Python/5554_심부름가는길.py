# baekjoon source = "https://www.acmicpc.net/problem/2935"
import sys

x, y = 0, 0
for i in range(4):
    time = int(sys.stdin.readline())
    x += time // 60
    y += time % 60
    if y > 59:
        x += y // 60
        y %= 60
print(x, y)
