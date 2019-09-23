# baekjoon source = "https://www.acmicpc.net/problem/12100"
import copy

'''
3
2 4 8
2 4 8
2 4 8

3
2 2 2
4 4 4
8 8 8
'''

def up(x):
    for j in range(n):
        i = 0
        while i < n - 1:
            if x[i][j] == 0:
                flag = False
                flag_two = False
                for z in range(i, n - 1):
                    flag = True
                    x[z][j] = x[z + 1][j]
                    if x[z + 1][j] != 0:
                        flag_two = True
                if flag:
                    x[z + 1][j] = 0
                if flag_two:
                    i -= 1
            else:
                for q in range(i+1,n):
                    if x[q][j] == 0:
                        continue
                    if x[i][j] == x[q][j]:
                        x[i][j] += x[q][j]
                        x[q][j] = 0
                        flag = False
                        for z in range(i + 1, n - 1):
                            flag = True
                            x[z][j] = x[z + 1][j]
                        if flag:
                            x[z + 1][j] = 0
                    break
            i += 1

def down(x):
    for j in range(n):
        i = n - 1
        while i > 0:
            if x[i][j] == 0:
                flag = False
                flag_two = False
                for z in range(i, 0, -1):
                    flag = True
                    x[z][j] = x[z - 1][j]
                    if x[z - 1][j] != 0:
                        flag_two = True
                if flag:
                    x[z - 1][j] = 0
                if flag_two:
                    i += 1
            else:
                for q in range(i-1,-1,-1):
                    if x[q][j] == 0:
                        continue
                    if x[i][j] == x[q][j]:
                        x[i][j] += x[q][j]
                        x[q][j] = 0
                        flag = False
                        for z in range(i - 1, 0, -1):
                            flag = True
                            x[z][j] = x[z - 1][j]
                        if flag:
                            x[z - 1][j] = 0
                    break
            i -= 1

def left(x):
    for j in range(n):
        i = 0
        while i < n - 1:
            if x[j][i] == 0:
                flag = False
                flag_two = False
                for z in range(i, n - 1):
                    flag = True
                    x[j][z] = x[j][z + 1]
                    if x[j][z + 1] != 0:
                        flag_two = True
                if flag:
                    x[j][z + 1] = 0
                if flag_two:
                    i -= 1

            else:
                for q in range(i + 1, n):
                    if x[j][q] == 0:
                        continue
                    if x[j][i] == x[j][q]:
                        x[j][i] += x[j][q]
                        x[j][q] = 0
                        flag = False
                        for z in range(i + 1, n - 1):
                            flag = True
                            x[j][z] = x[j][z + 1]
                        if flag:
                            x[j][z + 1] = 0
                    break

            i += 1

def right(x):
    for j in range(n):
        i = n - 1
        while i > 0:

            if x[j][i] == 0:
                flag = False
                flag_two = False
                for z in range(i, 0, -1):
                    flag = True
                    x[j][z] = x[j][z - 1]
                    if x[j][z - 1] != 0:
                        flag_two = True
                if flag:
                    x[j][z - 1] = 0
                if flag_two:
                    i += 1

            else:
                for q in range(i - 1, -1, -1):
                    if x[j][q] == 0:
                        continue
                    if x[j][i] == x[j][q]:
                        x[j][i] += x[j][q]
                        x[j][q] = 0
                        flag = False
                        for z in range(i - 1, 0, -1):
                            flag = True
                            x[j][z] = x[j][z - 1]
                        if flag:
                            x[j][z - 1] = 0
                    break

            # for aaa in x:
            #     print(aaa)
            # print()


            i -= 1

def solution(a, k, check):
    global result
    # for i in a:
    #     print(i)
    # print()
    if k == check:
        max_ = 0
        for i in a:
            max_ = max(max_, max(i))
        result = max(max_, result)
        return 0

    for i in range(4):
        # print(i,k)
        if i == 0:
            go = copy.deepcopy(a)
            up(go)
            solution(go, k + 1, check)
        elif i == 1:
            go = copy.deepcopy(a)
            down(go)
            solution(go, k + 1, check)
        elif i == 2:
            go = copy.deepcopy(a)
            left(go)
            solution(go, k + 1, check)
        else:
            go = copy.deepcopy(a)
            right(go)
            solution(go, k + 1, check)

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

solution(arr, 0, 5)

print(result)
