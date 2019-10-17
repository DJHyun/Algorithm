# baekjoon source = "https://www.acmicpc.net/problem/17406"

import sys
import itertools

def result_sum(x):
    global result
    for i in x:
        sum_ = sum(i)
        result = min(result, sum_)

def change_arr(matrix, x, y):
    for count in range(x // 2):
        i, j = count, count
        first = matrix[i][j]
        while not (i == count and j - 1 == count):
            if i < (x - count) - 1 and j == count:
                matrix[i][j] = matrix[i + 1][j]
                i += 1
            elif j < (y - count) - 1 and i == (x - count) - 1:
                matrix[i][j] = matrix[i][j + 1]
                j += 1
            elif i > count and j == (y - count) - 1:
                matrix[i][j] = matrix[i - 1][j]
                i -= 1
            elif j > count and i == count:
                matrix[i][j] = matrix[i][j - 1]
                j -= 1
        matrix[i][j] = first
    return matrix

def div(x):
    new_left_x = x[0] - x[2] - 1
    new_left_y = x[1] - x[2] - 1
    new_right_x = x[0] + x[2] - 1
    new_right_y = x[1] + x[2] - 1
    new_arr = []
    for i in range(new_left_x, new_right_x + 1):
        new_arr.append(test[i][new_left_y:new_right_y + 1])
    c = change_arr(new_arr, new_right_x - new_left_x + 1, new_right_y - new_left_y + 1)
    for i in range(new_left_x, new_right_x + 1):
        for j in range(new_left_y, new_right_y + 1):
            test[i][j] = c[i - new_left_x][j - new_left_y]

n, m, k = map(int, sys.stdin.readline().split())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
change = [list(map(int, sys.stdin.readline().split())) for _ in range(k)]
result = float('inf')

it = itertools.permutations(range(k))
for sol in it:
    test = [[0] * m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            test[x][y] = arr[x][y]
    for i in sol:
        div(change[i])
    result_sum(test)

print(result)
