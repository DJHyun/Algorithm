# baekjoon source = "https://www.acmicpc.net/problem/15684"

def check(x, y):
    if x < 0 or x > h : return False
    if y < 0 or y > n - 1: return False
    return True

def make_ladder(a,b):

    pass

def ladder(a, b):
    q = [[a, b]]
    visited = [[0] * n for _ in range(h +1)]

    while q:
        t = q.pop(0)
        # visited[t[0]+1][t[1]] = 1
        tx = t[0] + 1
        ty = t[1]
        if check(tx,ty):
            visited[tx][ty] = 1
            if arr[tx][ty] == 1:
                for i in range(2):
                    x = tx + dx[i]
                    y = ty + dy[i]
                    if check(x, y) and arr[x][y] == 1:
                        q.append([x, y])
                        visited[x][y]= 1
                        break
            else:
                q.append([tx, ty])
                visited[tx][ty] = 1

        for i in visited:
            print(i)
        print()
    if b == t[1]:
        return False
    else:
        return True


n, m, h = map(int, input().split())
arr = [[0] * n for _ in range(h + 1)]
dx, dy = [0, 0], [1, -1]
print(n, m, h)

for i in arr:
    print(i)
print()
for i in range(m):
    a, b = map(int, input().split())
    # if b%2:
    #     arr[a-1][b] = 1
    # else:
    arr[a][b - 1] = 1
    arr[a][b] = 1

for i in arr:
    print(i)
print()

idx = 0
while True:
    if ladder(0,idx):
        make_ladder(0,idx)
    else:
        idx += 1
