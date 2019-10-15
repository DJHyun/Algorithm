# baekjoon source = "https://www.acmicpc.net/problem/1753"

import sys
import heapq

v,e = map(int,sys.stdin.readline().split())
start = int(sys.stdin.readline())
arr = [[] for _ in range(v+1)]
for i in range(e):
    input_ = list(map(int,sys.stdin.readline().split()))
    arr[input_[0]].append([input_[1],input_[2]])

da = [[0]*3 for _ in range(v)]
da[0][1] = start
result = [0]*(v+1)
result[start] = 0
idx = 1
for i in range(1,v+1):
    if i == start:
        continue
    da[idx][1] = i
    da[idx][0] = float('INF')
    result[i] = float('INF')
    idx += 1

heapq.heapify(da)
while da:
    h = heapq.heappop(da)
    if result[h[1]] >= h[0]:
        for i in arr[h[1]]:
            if result[i[0]] >= i[1]+h[0]:
                result[i[0]] = i[1]+h[0]
                heapq.heappush(da,[result[i[0]],i[0],h[1]])

for i in range(1,v+1):
    if result[i] == float('INF'):
        print("INF")
    else:
        print(result[i])

