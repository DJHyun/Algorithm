# baekjoon source = "https://www.acmicpc.net/problem/1748"

import sys
N = sys.stdin.readline().strip()
result = 0
for i in range(len(N)-1):
    result += (i+1)*9*10**i
result += (int(N) - 10**(len(N)-1)+1)*len(N)
print(result)
