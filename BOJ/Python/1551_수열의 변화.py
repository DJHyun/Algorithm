# baekjoon source = "https://www.acmicpc.net/problem/1551"

import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
arr = list(map(int,sys.stdin.readline().split(',')))

for i in range(k):
    new = deque()
    for j in range(len(arr)-1):
        new.append(arr[j+1]-arr[j])
    arr = new


for i in range(n-k):
    if i != n-k-1:
        sys.stdout.write(str(arr[i]))
        sys.stdout.write(',')
    else:
        sys.stdout.write(str(arr[i]))