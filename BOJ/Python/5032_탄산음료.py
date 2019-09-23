# baekjoon source = "https://www.acmicpc.net/problem/5032"
import sys

e, f, c = map(int, sys.stdin.readline().split())
result = 0
e += f

while e >= c:
    result += (e // c)
    e = e//c + e%c

print(result)
