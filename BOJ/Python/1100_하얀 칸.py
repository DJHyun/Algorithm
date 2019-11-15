# baekjoon source = "https://www.acmicpc.net/problem/1100"

import sys

result = 0
for i in range(8):
    s = list(sys.stdin.readline().strip())
    for j in range(8):
        if i%2:
            if j%2:
                if s[j] == 'F':
                    result += 1
        else:
            if not j%2:
                if s[j] == 'F':
                    result += 1

print(result)
