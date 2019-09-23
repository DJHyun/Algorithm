# baekjoon source = "https://www.acmicpc.net/problem/2908"

import sys
numbers = list(sys.stdin.readline().rstrip().split())
for i,n in enumerate(numbers):
    numbers[i] = int(numbers[i][::-1])
print(max(numbers))