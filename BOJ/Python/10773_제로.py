# baekjoon source = "https://www.acmicpc.net/problem/10773"

import sys

k = int(sys.stdin.readline())
stack = [0] * 100000
top = -1
result = 0

for i in range(k):
    number = int(sys.stdin.readline())
    if number == 0:
        result -= stack[top]
        top -= 1
    else:
        top += 1
        stack[top] = number
        result += number

print(result)
