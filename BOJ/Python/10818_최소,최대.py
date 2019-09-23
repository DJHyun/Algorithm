# baekjoon source = "https://www.acmicpc.net/problem/10818"

import sys

n = int(sys.stdin.readline())
number = list(map(int,sys.stdin.readline().split()))
min_,max_ = number[0],number[0]
for i in range(1,n):
    if number[i] < min_:
        min_ = number[i]
    elif number[i] > max_:
        max_ = number[i]
print(min_,max_)
