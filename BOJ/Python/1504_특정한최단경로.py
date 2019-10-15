# baekjoon source = "https://www.acmicpc.net/problem/1504"

import sys
import heapq

v,e = map(int,sys.stdin.readline().split())

arr = [[0]*(v+1) for _ in range(v+1)]
for i in range(e):
    input_ = list(map(int,sys.stdin.readline().split()))
    arr[input_[0]][input_[1]] = input_[2]

one,two = map(int,sys.stdin.readline().split())
start = 1
r = 0
for cou in range(3):
    da = [[0]*3 for _ in range(v)]
    da[0][1] = start
    result = [0]*(v+1)
    result[start] = 0
    idx = 1

    for i in range(1,v+1):
        if i == start:
            continue
        result[i] = float('INF')

    heapq.heapify(da)
    while da:
        h = heapq.heappop(da)
        if result[h[1]] >= h[0]:
            for i in range(len(arr[h[1]])):
                if arr[h[1]][i] == 0:
                    continue
                if result[i] >= arr[h[1]][i]+h[0]:
                    result[i] = arr[h[1]][i]+h[0]
                    heapq.heappush(da,[result[i],i])
    if cou == 0:
        r += result[one]
        start = one
    elif cou == 1:
        r += result[two]
        start = two
    else:
        r += result[v]
print(r)