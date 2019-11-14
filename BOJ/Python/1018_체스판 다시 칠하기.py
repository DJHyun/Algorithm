# baekjoon source = "https://www.acmicpc.net/problem/1018"

import sys

def solution(x, y):
    one_count = 0
    two_count = 0

    for i in range(x, x + 8):
        for j in range(y, y + 8):
            if arr[i][j] != one[i - x][j - y]:
                one_count += 1

            if arr[i][j] != two[i - x][j - y]:
                two_count += 1

    return min(one_count, two_count)

n, m = map(int, sys.stdin.readline().split())
arr = [list(sys.stdin.readline().strip()) for _ in range(n)]

one = [['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W']]

two = [['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B'],
       ['B', 'W', 'B', 'W', 'B', 'W', 'B', 'W'],
       ['W', 'B', 'W', 'B', 'W', 'B', 'W', 'B']]

result = float('inf')
for i in range(n - 7):
    for j in range(m - 7):
        result = min(result, solution(i, j))
print(result)
