# baekjoon source = "https://www.acmicpc.net/problem/2580"

'''
0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
6 0 3 7 0 1 9 5 2
2 5 8 3 9 4 7 6 0

0 3 5 4 6 9 2 7 8
7 8 2 1 0 5 6 0 9
0 6 0 2 7 8 1 3 5
3 2 1 0 4 6 8 9 7
8 0 4 9 1 3 5 0 6
5 9 6 8 2 0 4 1 3
9 1 7 6 5 2 0 8 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0

'''
import sys

def backtracking(k, input):
    global flag
    c = [0] * 9
   
    if k == input:
        flag = False
        return flag
    else:
        k += 1
        candi = construct(k, c)
        
        for i in range(candi):
            if flag:
                arr[stack[k][0]][stack[k][1]] = c[i]

                for a in range(k+1,len(stack)):
                    arr[stack[a][0]][stack[a][1]] = 0


                backtracking(k, input)
                   
def construct(k, c):
    in_perm = [1] * 10

    for i in range(9):
        in_perm[arr[stack[k][0]][i]] = 0

    for i in range(9):
        in_perm[arr[i][stack[k][1]]] = 0

    for i in range(3):
        for j in range(3):
            in_perm[arr[stack[k][0] + i - stack[k][0]%3][stack[k][1] + j - stack[k][1]%3]] = 0
    
    ncandi = 0

    for i in range(1,10):
        if in_perm[i]:
            c[ncandi] = i
            ncandi += 1

    return ncandi

arr = [list(map(int,sys.stdin.readline().split())) for _ in range(9)]
count = 0
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            count += 1
stack, top = [0] * count, -1
flag = True
for i in range(9):
    for j in range(9):
        if arr[i][j] == 0:
            top += 1
            stack[top] = (i,j)
backtracking(-1,count-1)

for i in arr:
    print(' '.join(map(str,i)))
