# baekjoon source = "https://www.acmicpc.net/problem/5618"

import sys

n = int(sys.stdin.readline())
num = list(map(int,sys.stdin.readline().split()))
min_ = num.pop(num.index(min(num)))

for i in range(1,min_+1):
    if not min_%i:
        for j in range(n-1):
            if num[j]%i:
                break
        else:
            print(i)
