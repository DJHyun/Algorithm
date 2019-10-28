# baekjoon source = "https://www.acmicpc.net/problem/7562"
'''
3
8
0 0
7 0
100
0 0
30 50
10
1 1
1 1
'''
import sys
from collections import deque

def check(x, y):
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    if visited[x][y]: return False
    return True

def solution(x, y):
    tq = [[x, y]]
    score = 0

    while tq:
        q = deque(tq[:])
        tq.clear()
        score += 1
        while q:
            t = q.popleft()
            for i in range(8):
                tx = t[0] + dx[i]
                ty = t[1] + dy[i]
                if check(tx, ty):
                    if [tx, ty] == end:
                        return score
                    visited[tx][ty] = 1
                    tq.append([tx, ty])


t = int(sys.stdin.readline())
dx, dy = [1, 1, 2, 2, -1, -1, -2, -2], [-2, 2, -1, 1, -2, 2, -1, 1]
for tc in range(t):
    n = int(sys.stdin.readline())
    visited = [[0] * n for _ in range(n)]
    start = list(map(int, sys.stdin.readline().split()))
    end = list(map(int, sys.stdin.readline().split()))

    if start == end:
        print(0)
    else:
        print(solution(start[0], start[1]))
