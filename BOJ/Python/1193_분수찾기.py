# baekjoon source = "https://www.acmicpc.net/problem/1193"

import sys

X = int(sys.stdin.readline().strip())
cnt = 1
result = 0
for i in range(1, X+1):
    if 1+(i-1)*i/2 > X:
        cnt = i-1
        break
    elif 1+(i-1)*i/2 == X:
        cnt = i

n = int(1+(cnt-1)*cnt/2)

if cnt % 2:
    result = cnt-(X-n)
    result2 = (cnt+1)-result
else:
    result2 = cnt-(X-n)
    result = (cnt+1)-result2

print(f'{result}/{result2}')