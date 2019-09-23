# baekjoon source = "https://www.acmicpc.net/problem/1966"
'''
3
1 0
5
4 2
1 2 3 4
4 2
2 1 4 3
'''
import sys

T = int(sys.stdin.readline())
for _ in range(1, T + 1):

    N, M = map(int,sys.stdin.readline().split())
    q = list(map(int,sys.stdin.readline().split()))
    for i in range(N):
        q[i] = (q[i],i)

    idx = 0
    while q:
        if q[0] == max(q,key=lambda x: x[0]):
            t = q.pop(0)
            idx += 1
            if t[1] == M:
                break
        else:
            q.append(q.pop(0))

    print(idx)



