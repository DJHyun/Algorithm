# baekjoon source = "https://www.acmicpc.net/problem/3055"
import sys
from collections import deque

def check(x, y):
    if x < 0 or x > r - 1: return False
    if y < 0 or y > c - 1: return False
    if arr[x][y] == 'X': return False
    return True

def solution(w, s):
    tq = w
    tq.append(s + [-1])
    score = 0
    while tq:
        q = deque(tq[:])
        tq.clear()
        while q:
            t = q.popleft()
            for i in range(4):
                tx = t[0] + dx[i]
                ty = t[1] + dy[i]
                if len(t) == 3:
                    tz = t[2]
                else:
                    tz = 0
                if tz == 0:
                    if check(tx, ty) and arr[tx][ty] == '.':
                        tq.append([tx, ty])
                        arr[tx][ty] = '*'
                else:
                    if check(tx, ty) and (arr[tx][ty] == '.' or arr[tx][ty] == 'D'):
                        if arr[tx][ty] == 'D':
                            return score + 1
                        tq.append([tx, ty, -1])
                        arr[tx][ty] = 'S'

        score += 1

    return 'KAKTUS'

r, c = map(int, sys.stdin.readline().split())
arr = [[''] * c for _ in range(r)]
water = []
start = [0, 0]
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
for i in range(r):
    inp = list(sys.stdin.readline().strip())
    for j in range(c):
        arr[i][j] = inp[j]
        if inp[j] == '*':
            water.append([i, j])
        elif inp[j] == 'S':
            start[0] = i
            start[1] = j

print(solution(water, start))
