# baekjoon source = "https://www.acmicpc.net/problem/1002"
import math

n = int(input())
for i in range(n):
    x, y, r, a, b, c = map(int, input().split())
    sum_ = r + c
    sub = abs(r - c)
    d = math.sqrt((x - a) ** 2 + (y - b) ** 2)

    if x == a and y == b and r == c:
        print(-1)
    elif sum_ > d and sub < d:
        print(2)
    elif sum_ == d or sub == d:
        print(1)
    else:
        print(0)
