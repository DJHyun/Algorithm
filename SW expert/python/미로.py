import sys
sys.stdin = open("미로.txt", "r")

def st(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 2:
                return (i,j)

def ta(arr):
    for i in range(len(arr)):
        for j in range(len(arr)):
            if arr[i][j] == 3:
                return (i,j)

def dfs(dot):
    global dx,dy
    
    visited[dot[0]][dot[1]] = 1

    for i in range(4):
        x,y,ss,sf = dx[i],dy[i],dot[0],dot[1]
        if ss+x < 0 or ss+x > N-1 or sf + y < 0 or sf + y > N-1:
            continue
        else:
            if visited[ss+x][sf+y]:
                continue
            elif miro[ss+x][sf+y] == 3:
                visited[ss+x][sf+y] = 1
                return 1
            elif miro[ss+x][sf+y] == 0:
                dfs((ss+x,sf+y))

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    miro = [list(map(int,input())) for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    stdot = st(miro)
    fidot = ta(miro)
    dx, dy = [0,-1,0,1],[1,0,-1,0]
    
    dfs(stdot)
    if visited[fidot[0]][fidot[1]]:
        print(f'#{test_case} 1')
    else:
        print(f'#{test_case} 0')