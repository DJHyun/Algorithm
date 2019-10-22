# baekjoon source = "https://www.acmicpc.net/problem/1022"
import sys

a, b, c, d = map(int, sys.stdin.readline().split())
arr = [[0] * 5 for _ in range(50)]
e, f = abs(a - c) + 1, abs(b - d) + 1
result = e * f
x, y = 0, 0
val = 1

if a <= x <= c and b <= y <= d:
    arr[x - a][y - b] = str(val)
    result -= 1

dir = -1
len_ = 0
dx, dy = [0, -1, 0, 1], [1, 0, -1, 0]
max_ = 0
while result > 0:
    dir = (dir + 1) % 4
    if dir == 0 or dir == 2:
        len_ += 1
    for i in range(len_):
        val += 1
        x += dx[dir]
        y += dy[dir]
        if a <= x <= c and b <= y <= d:
            arr[x - a][y - b] = str(val)
            result -= 1
            max_ = len(str(val))

for i in range(e):
    for j in range(f):
        check = len(arr[i][j])
        if check < max_:
            go = max_ - check
            sys.stdout.write(' ' * go + arr[i][j]+' ')
        else:
            sys.stdout.write(arr[i][j]+' ')
    sys.stdout.write('\n')
