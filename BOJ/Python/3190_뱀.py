# baekjoon source = "https://www.acmicpc.net/problem/3190"
'''
6
3
3 4
2 5
5 3
3
3 D
15 L
17 D

9

10
4
1 2
1 3
1 4
1 5
4
8 D
10 D
11 D
13 L

21
'''

def direction(a, b):
    if a == 0:
        if b == 'D':
            a = 1
        else:
            a = 3
    elif a == 1:
        if b == 'D':
            a = 2
        else:
            a = 0
    elif a == 2:
        if b == 'D':
            a = 3
        else:
            a = 1
    else:
        if b == 'D':
            a = 0
        else:
            a = 2
    return a

def solution(x, y):
    if x < 0 or x > n - 1: return True
    if y < 0 or y > n - 1: return True
    if arr[x][y] == 2: return True
    return False

n = int(input())
arr = [[0] * n for _ in range(n)]
k = int(input())
for i in range(k):
    apple = list(map(int, input().split()))
    arr[apple[0] - 1][apple[1] - 1] = 1
arr[0][0] = 2

l = int(input())
d = [list(input().split()) for _ in range(l)]

x, y = 0, 0
dd = 0
result_flag = True
result = 0
i = 0
snake = [[0,0]]
while True:
    if result_flag:

        if i == 0:
            dd = 0
        else:
            dd = direction(dd, d[i - 1][1])

        while True:
            if i < l:
                if result == int(d[i][0]):
                    break
            result += 1

            flag = False
            if dd == 0:
                y += 1
                if solution(x, y):
                    result_flag = False
                    break
                if arr[x][y] == 1:
                    arr[x][y] = 2
                    snake.append([x, y])
                else:
                    po = snake.pop(0)
                    arr[x][y], arr[po[0]][po[1]] = arr[po[0]][po[1]], arr[x][y]
                    snake.append([x,y])
            elif dd == 1:
                x += 1
                if solution(x, y):
                    result_flag = False
                    break
                if arr[x][y] == 1:
                    arr[x][y] = 2
                    snake.append([x, y])
                else:
                    po = snake.pop(0)
                    arr[x][y], arr[po[0]][po[1]] = arr[po[0]][po[1]], arr[x][y]
                    snake.append([x, y])
            elif dd == 2:
                y -= 1
                if solution(x, y):
                    result_flag = False
                    break
                if arr[x][y] == 1:
                    arr[x][y] = 2
                    snake.append([x, y])
                else:
                    po = snake.pop(0)
                    arr[x][y], arr[po[0]][po[1]] = arr[po[0]][po[1]], arr[x][y]
                    snake.append([x, y])
            else:
                x -= 1
                if solution(x, y):
                    result_flag = False
                    break
                if arr[x][y] == 1:
                    arr[x][y] = 2
                    snake.append([x, y])
                else:
                    po = snake.pop(0)
                    arr[x][y], arr[po[0]][po[1]] = arr[po[0]][po[1]], arr[x][y]
                    snake.append([x, y])
        i += 1
    else:
        break

print(result)
