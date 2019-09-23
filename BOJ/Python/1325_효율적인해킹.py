'''
5 4
3 1
3 2
4 3
5 3

5 2
4 1
5 2

3 3
3 2
2 1
1 3

50 2
2 1
1 2
'''

import sys

def bfs(a):
    global count
    q_front = -1
    q_last = -1
    q = [0] * N
    visited = [0] * (N + 1)
    q_last += 1
    q[q_last] = a
    visited[a] = 1
    count = 1
    while True:
        if q_front == q_last:
            break
        q_front += 1
        t = q[q_front]
        for i in arr[t]:
            if not visited[i]:
                q_last += 1
                q[q_last] = i
                visited[i] = 1
                count += 1

N, M = map(int, sys.stdin.readline().split())
arr = [[] for _ in range(N+1)]
top = -1
max_ = 0
result = []

for _ in range(M):
    n, m = map(int, sys.stdin.readline().split())
    arr[m].append(n)

for i in range(1,N+1):
    count = 0
    bfs(i)
    if max_ < count:
        max_ = count
        result.clear()
        result.append(i)
    elif max_ == count:
        result.append(i)

print(' '.join(list(map(str, result))))
