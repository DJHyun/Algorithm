# baekjoon source = "https://www.acmicpc.net/problem/7576"
'''
6 4
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 1

6 4
1 -1 0 0 0 0
0 -1 0 0 0 0
0 0 0 0 -1 0
0 0 0 0 -1 1
'''
import sys
import collections
import copy

def check(x, y):
    if x < 0 or x > N-1 : return False
    if y < 0 or y > M-1 : return False
    if tomato[x][y] == -1  : return False
    return True

def bfs(arr,st):
    mq = collections.deque([])
    idx = 0
    for i in range(len(st)):
        mq.append(st[i])
        visited[st[i][0]][st[i][1]] = 1
    
    while mq:
        que = copy.copy(mq)
        while que:
            t = que.popleft()
            mq.popleft()
            for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if check(x,y) and not visited[x][y]:
                    mq.append((x,y))
                    visited[x][y] = 1
        idx += 1
    return idx

M, N = map(int,sys.stdin.readline().split())
tomato = [list(map(int,sys.stdin.readline().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]
st = []
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

for i in range(N):
    for j in range(M):
        if tomato[i][j] == -1:
            visited[i][j] = -1
        elif tomato[i][j] == 1:
            st.append((i,j))

d = bfs(tomato,st) - 1
flag = True
for i in range(N):
    for j in range(M):
        if visited[i][j] == 0:
            flag = False
            break

if flag:
    print(d)
else:
    print(-1)