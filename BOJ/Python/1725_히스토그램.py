# baekjoon source = "https://www.acmicpc.net/problem/1725"
import itertools





n = int(input())
stack = []
numbers = [0] * n
for i in range(n):
    numbers[i] = int(input())
result = float('-inf')
i = 0
while i < n:
    while stack and numbers[stack[len(stack) - 1]] > numbers[i]:
        p = stack.pop()
        h = numbers[p]
        w = i
        if stack:
            w = i - stack[len(stack) - 1] - 1
        result = max(result, h * w)

    stack.append(i)
    i += 1
while stack:
    p = stack.pop()
    h = numbers[p]
    w = n
    if stack:
        w = i - stack[len(stack) - 1] - 1
    result = max(result, h * w)
print(result)
