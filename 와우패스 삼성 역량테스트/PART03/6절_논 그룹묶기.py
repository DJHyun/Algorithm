'''
7
8
1 1 1 0 1 1 0 0
0 0 1 0 0 1 1 1
0 1 1 1 0 1 1 0
1 1 1 0 0 1 1 0
0 0 0 0 0 0 0 0
0 1 1 1 1 0 1 1
1 1 1 0 0 1 0 0
1 1 0 0 1 1 1 0
7
1 1 1 0 1 1 0
0 0 1 0 0 1 1
0 1 1 1 0 1 1
1 1 1 0 0 1 1
0 0 0 0 0 0 0
0 1 1 1 1 0 1
1 1 1 0 0 1 0
5
1 1 1 0 1
0 0 1 0 0
0 1 1 1 0
1 1 1 0 0
0 0 0 0 0
7
1 1 1 0 1 1 0
0 0 1 0 0 1 1
0 1 1 1 0 1 1
1 1 1 0 0 1 1
0 0 0 0 0 0 0
0 1 1 1 1 0 1
1 1 1 0 0 1 0
10
1 1 1 0 1 1 1 1 0 1
0 0 1 0 0 0 1 1 1 0
1 1 1 0 0 0 0 0 0 0
0 0 1 0 0 1 1 1 0 1
0 0 1 0 0 0 1 1 1 0
1 1 1 0 0 0 0 0 0 0
0 1 1 1 0 1 1 1 0 0
0 0 0 0 0 1 1 1 0 1
0 0 1 0 0 0 1 1 1 0
1 1 1 0 0 0 0 0 0 0
9
1 1 1 0 1 1 1 1 0
0 0 1 0 0 0 1 1 1
1 1 1 0 0 0 0 0 0
0 0 1 0 0 1 1 1 0
0 0 1 0 0 0 1 1 1
1 1 1 0 0 0 0 0 0
0 1 1 1 0 1 1 1 0
0 0 0 0 0 1 1 1 0
0 0 1 0 0 0 5 5 5
6
1 1 1 0 1 1
0 0 1 0 0 0
1 1 1 0 0 0
0 0 1 0 0 1
0 0 1 0 0 0
1 1 1 0 0 0
'''

from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if arr[x][y] != 1: return False
    return True

def solution(x, y):
    q = deque([[x, y]])
    score = 1
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx,ty):
                arr[tx][ty] = 2
                q.append([tx,ty])
                score += 1

    return str(score)

t = int(input())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]
for tc in range(1, t + 1):

    n = int(input())
    arr = [list(map(int, input().strip().split())) for _ in range(n)]
    size = []
    result = 0

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                arr[i][j] = 2
                size.append(solution(i,j))
                result += 1

    print('#{} {} {}'. format(tc, result, ' '.join(size)))
