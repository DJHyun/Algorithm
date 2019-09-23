# baekjoon source = "https://www.acmicpc.net/problem/15683"
def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if arr[x][y] == 6: return False
    return True

def solution(v, x, y):
    global max_

    q = [[x, y]]
    while q:
        print(q)
        t = q.pop(0)
        max_cnt = float('-inf')
        idx = 0
        if v == 1:
            for i in range(4):
                cnt = 0
                for j in range(max_):
                    tx = t[0] + dx[v - 1][i][j]
                    ty = t[1] + dy[v - 1][i][j]
                    if check(tx, ty):
                        cnt += 1
                    else:
                        break
                if max_cnt < cnt:
                    max_cnt = cnt
                    idx = i
            for j in range(max_):
                tx = t[0] + dx[0][idx][j]
                ty = t[1] + dy[0][idx][j]
                if check(tx, ty):
                    arr[tx][ty] = 1
                else:
                    break

    for i in arr:
        print(i)

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
max_ = max(n, m)
dx_one = [[0] * max_, [0] * max_, list(range(1, max_ + 1)), list(range(-1, -(max_ + 1), -1))]
dy_one = [list(range(1, max_ + 1)), list(range(-1, -(max_ + 1), -1)), [0] * max_, [0] * max_]
a = list(range(1, max_ + 1))
b = list(range(-1, -(max_ + 1), -1))
dx_two = [[0] * (max_ * 2), a + b]
dy_two = [a + b, [0] * (max_ * 2)]
dx_three = []
dy_three = []

print(dx_one)
print(dy_one)
print(dx_two)
print(dy_two)

print(n, m)
for i in arr:
    print(i)

# for i in range(n):
#     for j in range(m):
#         if arr[i][j] != 0 and arr[i][j] != 6:
#             solution(arr[i][j], i, j)
