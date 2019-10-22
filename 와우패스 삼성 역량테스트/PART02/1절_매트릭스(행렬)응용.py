'''
3
7
0 0 1 5 3 5 5 6,1 1 2 4 5 2,3 2 5 5
4
0 1 1 3,2 2,2 3 3 3
5
0 0 3 4 2 4,1 2 4 2,3 2 4 4
'''

import sys

t = int(sys.stdin.readline())
dx, dy = [0, 0, 1, -1], [1, -1, 0, 0]

def c(x, y):
    if x < 0 or x > size - 1: return False
    if y < 0 or y > size - 1: return False
    return True

def solution(x, y, m):
    for i in range(4):
        tx = x
        ty = y
        for j in range(m):
            tx += dx[i]
            ty += dy[i]
            if c(tx,ty):
                arr[tx][ty] = 1

for test_case in range(t):
    size = int(sys.stdin.readline())
    arr = [[0] * size for _ in range(size)]
    check = sys.stdin.readline().strip().split(',')
    len_ = len(check)
    for i in range(len_):
        check[i] = list(map(int, check[i].split()))
    for i in range(len_):
        for j in range(0, len(check[i]), 2):
            arr[check[i][j]][check[i][j+1]] = 1
            solution(check[i][j],check[i][j+1],i+1)
    count = 0
    for i in arr:
        for j in i:
            if j == 0:
                count += 1
    print(count)
