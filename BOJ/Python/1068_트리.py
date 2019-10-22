# baekjoon source = "https://www.acmicpc.net/problem/1068"

'''
12
1 4 3 -1 3 1 2 0 6 6 6 1
2
'''
import sys

def solution(x):
    if not visited[x]:
        for i in range(1, len(mst[x])):
            solution(mst[x][i])
        visited[x] = 1
        mst[x] = -1

n = int(sys.stdin.readline())
mst = list(map(int, sys.stdin.readline().split()))
delete = int(sys.stdin.readline())
visited = [0] * n
result = 0

for i in range(n):
    mst[i] = [mst[i]]

for i in range(n):
    if mst[i][0] == -1:
        continue
    mst[mst[i][0]].append(i)

if mst[delete][0] != -1:
    mst[mst[delete][0]].remove(delete)
    solution(delete)
    for i in mst:
        if i == -1:
            continue
        if len(i) == 1:
            result += 1

    print(result)
else:
    print(0)

