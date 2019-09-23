# baekjoon source = "https://www.acmicpc.net/problem/3986"

import sys

n = int(sys.stdin.readline())
result = 0

for _ in range(n):
    s = sys.stdin.readline().strip()
    stack = [''] * len(s)
    top = -1

    for i in s:
        if top == -1:
            top += 1
            stack[top] = i
        elif i == stack[top]:
            stack[top] = ''
            top -= 1
        else:
            top += 1
            stack[top] = i

    if stack[0] == '':
        result += 1

print(result)
