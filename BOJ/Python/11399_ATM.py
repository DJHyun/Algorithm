# baekjoon source = "https://www.acmicpc.net/problem/11399"

import sys
N = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()));num.sort();result = 0
for i in range(N):
    result += sum(num[:i+1])
print(result)




