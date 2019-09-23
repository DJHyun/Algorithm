import sys
sys.stdin = open("미로의거리.txt", "r")

def check(x,y):
    if x < 0 or x > N - 1: return False
    if y < 0 or y > N - 1: return False
    if matrix[x][y] == 1: return False
    return True

def bfs(matrix, start, finish):
    tq = []
    result = 0
    tq.append(start)
    visited[start[0]][start[1]] = 1
    
    while tq:
        q = tq[:]
        tq = []
        while q:
            t = q.pop(0)
            for i in range(4):
                x = t[0] + dx[i]
                y = t[1] + dy[i]
                if check(x,y) and not visited[x][y]:
                    if matrix[x][y] == 3:
                        q = []
                        tq = []
                        return result
                    else:
                        tq.append((x,y))
                        visited[x][y] = 1
        result += 1

    return 0

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int,input())) for _ in range(N)]
    start, finish = 0,0
    visited = [[0]*N for _ in range(N)]
    dx, dy = [1,-1,0,0],[0,0,1,-1]

    for i in range(N):
        for j in range(N):
            if matrix[i][j] == 2:
                start = (i,j)
            elif matrix[i][j] == 3:
                finish = (i,j)
    
    print(f'#{test_case} {bfs(matrix,start,finish)}')