# baekjoon source = "https://www.acmicpc.net/problem/5373"
'''
6
1
U-
1
U+
1
D-
1
D+
1
F+
1
F-
X
4
1
L-
2
F+ B+
4
U- D- L+ R+
10
L- U- L+ U- L- U- U- L+ U+ U+
'''

import sys

T = int(input())
for test_case in range(1, T + 1):
    up = [['w'] * 3 for _ in range(3)]
    front = [['r'] * 3 for _ in range(3)]
    down = [['y'] * 3 for _ in range(3)]
    left = [['g'] * 3 for _ in range(3)]
    right = [['b'] * 3 for _ in range(3)]
    back = [['o'] * 3 for _ in range(3)]

    n = int(input())
    check = input().split()

    for i in range(n):
        if check[i][1] == '-':
            if check[i][0] == 'U':
                tmp = front[0][:]
                front[0] = left[0][:]
                left[0] = back[0][:]
                back[0] = right[0][:]
                right[0] = tmp[:]

                tmp = up[0][0][:]
                up[0][0] = up[0][2][:]
                up[0][2] = up[2][2][:]
                up[2][2] = up[2][0][:]
                up[2][0] = tmp[:]

                tmp = up[0][1][:]
                up[0][1] = up[1][2][:]
                up[1][2] = up[2][1][:]
                up[2][1] = up[1][0][:]
                up[1][0] = tmp[:]

            elif check[i][0] == 'D':
                tmp = front[2][:]
                front[2] = right[2][:]
                right[2] = back[2][:]
                back[2] = left[2][:]
                left[2] = tmp[:]

                tmp = down[0][0][:]
                down[0][0] = down[0][2][:]
                down[0][2] = down[2][2][:]
                down[2][2] = down[2][0][:]
                down[2][0] = tmp[:]

                tmp = down[0][1][:]
                down[0][1] = down[1][2][:]
                down[1][2] = down[2][1][:]
                down[2][1] = down[1][0][:]
                down[1][0] = tmp[:]

            elif check[i][0] == 'F':
                tmp = up[2][:]
                for a in range(3):
                    up[2][a] = right[a][0][:]
                for a in range(3):
                    right[a][0] = down[0][2 - a][:]
                for a in range(3):
                    down[0][a] = left[2][a][:]
                for a in range(3):
                    left[a][2] = tmp[2 - a][:]

                tmp = front[0][0][:]
                front[0][0] = front[0][2][:]
                front[0][2] = front[2][2][:]
                front[2][2] = front[2][0][:]
                front[2][0] = tmp[:]

                tmp = front[0][1][:]
                front[0][1] = front[1][2][:]
                front[1][2] = front[2][1][:]
                front[2][1] = front[1][0][:]
                front[1][0] = tmp[:]

            elif check[i][0] == 'B':
                tmp = up[0][:]
                for a in range(3):
                    up[0][a] = left[2 - a][0][:]
                for a in range(3):
                    left[a][0] = down[2][a][:]
                for a in range(3):
                    down[2][a] = right[2 - a][2][:]
                for a in range(3):
                    right[a][2] = tmp[a][:]

                tmp = back[0][0][:]
                back[0][0] = back[0][2][:]
                back[0][2] = back[2][2][:]
                back[2][2] = back[2][0][:]
                back[2][0] = tmp[:]

                tmp = back[0][1][:]
                back[0][1] = back[1][2][:]
                back[1][2] = back[2][1][:]
                back[2][1] = back[1][0][:]
                back[1][0] = tmp[:]

            elif check[i][0] == 'L':
                tmp = []

                for a in range(3):
                    tmp.append(up[a][0][:])
                for a in range(3):
                    up[a][0] = front[a][0][:]
                for a in range(3):
                    front[a][0] = down[a][0][:]
                for a in range(3):
                    down[a][0] = back[2 - a][2][:]
                for a in range(3):
                    back[a][2] = tmp[2 - a][:]

                tmp = left[0][0][:]
                left[0][0] = left[0][2][:]
                left[0][2] = left[2][2][:]
                left[2][2] = left[2][0][:]
                left[2][0] = tmp[:]

                tmp = left[0][1][:]
                left[0][1] = left[1][2][:]
                left[1][2] = left[2][1][:]
                left[2][1] = left[1][0][:]
                left[1][0] = tmp[:]

            else:
                tmp = []
                for a in range(3):
                    tmp.append(up[a][2][:])
                for a in range(3):
                    up[a][2] = back[2 - a][0][:]
                for a in range(3):
                    back[a][0] = down[2 - a][2][:]
                for a in range(3):
                    down[a][2] = front[a][2][:]
                for a in range(3):
                    front[a][2] = tmp[a][:]

                tmp = right[0][0][:]
                right[0][0] = right[0][2][:]
                right[0][2] = right[2][2][:]
                right[2][2] = right[2][0][:]
                right[2][0] = tmp[:]

                tmp = right[0][1][:]
                right[0][1] = right[1][2][:]
                right[1][2] = right[2][1][:]
                right[2][1] = right[1][0][:]
                right[1][0] = tmp[:]
        else:
            if check[i][0] == 'U':
                tmp = front[0][:]
                front[0] = right[0][:]
                right[0] = back[0][:]
                back[0] = left[0][:]
                left[0] = tmp[:]

                tmp = up[0][0][:]
                up[0][0] = up[2][0][:]
                up[2][0] = up[2][2][:]
                up[2][2] = up[0][2][:]
                up[0][2] = tmp[:]

                tmp = up[0][1][:]
                up[0][1] = up[1][0][:]
                up[1][0] = up[2][1][:]
                up[2][1] = up[1][2][:]
                up[1][2] = tmp[:]

            elif check[i][0] == 'D':
                tmp = front[2][:]
                front[2] = left[2][:]
                left[2] = back[2][:]
                back[2] = right[2][:]
                right[2] = tmp[:]

                tmp = down[0][0][:]
                down[0][0] = down[2][0][:]
                down[2][0] = down[2][2][:]
                down[2][2] = down[0][2][:]
                down[0][2] = tmp[:]

                tmp = down[0][1][:]
                down[0][1] = down[1][0][:]
                down[1][0] = down[2][1][:]
                down[2][1] = down[1][2][:]
                down[1][2] = tmp[:]

            elif check[i][0] == 'F':
                tmp = up[2][:]
                for a in range(3):
                    up[2][a] = left[2 - a][2][:]
                for a in range(3):
                    left[a][2] = down[0][a][:]
                for a in range(3):
                    down[0][a] = right[2 - a][0][:]
                for a in range(3):
                    right[a][0] = tmp[a][:]

                tmp = front[0][0][:]
                front[0][0] = front[2][0][:]
                front[2][0] = front[2][2][:]
                front[2][2] = front[0][2][:]
                front[0][2] = tmp[:]

                tmp = front[0][1][:]
                front[0][1] = front[1][0][:]
                front[1][0] = front[2][1][:]
                front[2][1] = front[1][2][:]
                front[1][2] = tmp[:]

            elif check[i][0] == 'B':
                tmp = up[0][:]
                for a in range(3):
                    up[0][a] = right[a][2][:]
                for a in range(3):
                    right[a][2] = down[2][2 - a][:]
                for a in range(3):
                    down[2][a] = left[a][0][:]
                for a in range(3):
                    left[a][0] = tmp[2 - a][:]

                tmp = back[0][0][:]
                back[0][0] = back[2][0][:]
                back[2][0] = back[2][2][:]
                back[2][2] = back[0][2][:]
                back[0][2] = tmp[:]

                tmp = back[0][1][:]
                back[0][1] = back[1][0][:]
                back[1][0] = back[2][1][:]
                back[2][1] = back[1][2][:]
                back[1][2] = tmp[:]

            elif check[i][0] == 'L':
                tmp = []
                for a in range(3):
                    tmp.append(up[a][0][:])
                for a in range(3):
                    up[a][0] = back[2 - a][2][:]
                for a in range(3):
                    back[a][2] = down[2 - a][0][:]
                for a in range(3):
                    down[a][0] = front[a][0][:]
                for a in range(3):
                    front[a][0] = tmp[a][:]

                tmp = left[0][0][:]
                left[0][0] = left[2][0][:]
                left[2][0] = left[2][2][:]
                left[2][2] = left[0][2][:]
                left[0][2] = tmp[:]

                tmp = left[0][1][:]
                left[0][1] = left[1][0][:]
                left[1][0] = left[2][1][:]
                left[2][1] = left[1][2][:]
                left[1][2] = tmp[:]

            else:
                tmp = []
                for a in range(3):
                    tmp.append(up[a][2][:])
                for a in range(3):
                    up[a][2] = front[a][2][:]
                for a in range(3):
                    front[a][2] = down[a][2][:]
                for a in range(3):
                    down[a][2] = back[2 - a][0][:]
                for a in range(3):
                    back[a][0] = tmp[2 - a][:]

                tmp = right[0][0][:]
                right[0][0] = right[2][0][:]
                right[2][0] = right[2][2][:]
                right[2][2] = right[0][2][:]
                right[0][2] = tmp[:]

                tmp = right[0][1][:]
                right[0][1] = right[1][0][:]
                right[1][0] = right[2][1][:]
                right[2][1] = right[1][2][:]
                right[1][2] = tmp[:]

    for i in up:
        print(''.join(i))
