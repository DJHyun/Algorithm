import sys

sys.stdin = open("5250_최소비용.txt", "r")

def check(x, y):
    global n

    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

def bfs(x, y, h):
    q = []
    q.append([x, y, h])
    visited[x][y] = 0

    while q:
        t = q.pop(0)
        # if t[0] == n - 1 and t[1] == n - 1:
        #     return visited[t[0]][t[1]]
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx, ty):
                v = visited[t[0]][t[1]]
                if visited[tx][ty] == -1:
                    if arr[tx][ty] > t[2]:
                        q.append([tx, ty, arr[tx][ty]])
                        visited[tx][ty] = v + 1 + (arr[tx][ty] - t[2])
                    else:
                        q.append([tx, ty, arr[tx][ty]])
                        visited[tx][ty] = v + 1
                else:
                    if arr[tx][ty] > t[2]:
                        if v + 1 + (arr[tx][ty] - t[2]) < visited[tx][ty]:
                            q.append([tx, ty, arr[tx][ty]])
                            visited[tx][ty] = v + 1 + (arr[tx][ty] - t[2])
                    else:
                        if v + 1 < visited[tx][ty]:
                            q.append([tx, ty, arr[tx][ty]])
                            visited[tx][ty] = v + 1

    return visited[n-1][n-1]

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [[-1] * n for _ in range(n)]
    dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

    print(f'#{test_case} {bfs(0, 0, arr[0][0])}')
