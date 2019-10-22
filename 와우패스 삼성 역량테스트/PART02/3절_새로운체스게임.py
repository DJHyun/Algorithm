'''
3
7
0 0 1 5 5 6,2 4 5 2,3 2 5 5
4
1 3,2 2,2 3 3 3
5
0 0 3 4 2 4,1 2 4 2,3 2 4 4
'''
import sys

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

def solution(x, y, m):
    for i in range(8):
        tx = x
        ty = y
        for j in range(m):
            tx += dx[i]
            ty += dy[i]
            if check(tx,ty):
                arr[tx][ty] = 1

t = int(sys.stdin.readline())
dx, dy = [0, 0, 1, -1, 1, 1, -1, -1], [1, -1, 0, 0, 1, -1, 1, -1]
for tc in range(t):
    n = int(sys.stdin.readline())
    arr = [[0] * n for _ in range(n)]
    queen = sys.stdin.readline().strip().split(',')
    len_ = len(queen)
    for i in range(len_):
        queen[i] = list(map(int, queen[i].split()))

    for i in range(len_):
        for j in range(0, len(queen[i]), 2):
            arr[queen[i][j]][queen[i][j + 1]] = 1
            solution(queen[i][j], queen[i][j + 1], i + 1)

    count = 0
    for i in arr:
        for j in i:
            if j == 0:
                count += 1
    print(count)