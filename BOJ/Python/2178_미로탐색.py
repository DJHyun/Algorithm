# baekjoon source = "https://www.acmicpc.net/problem/2178"

import sys

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > m - 1: return False
    if arr[x][y] == '0': return False
    return True

def solution(a):
    q = [a]
    index = 2
    while q:
        length = len(q)
        for idx in range(length):
            t = q.pop(0)
            for i in range(4):
                x = t // 100 + dx[i]
                y = t % 100 + dy[i]
                if x == n-1 and y == m-1:
                    return index
                if check(x, y):
                    arr[x][y] = '0'
                    q.append(x * 100 + y)
        index += 1

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]

print(solution(0))
