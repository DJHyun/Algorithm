'''
3
9 5
P P P P P P P P P
P P P B P P P P P
P P P B B B B P P
P B B B B B B P P
P P P B B B B B P
P P P B P B B B P
P B P P P B P P P
P B B P B P B P P
P P P P P P P P P
9 10
P P P P P P P P P
P P B B P P P P P
P P P B B B B P P
P B B B B B B P P
P P P B B B B B P
P P P B P B B B P
P B P P B B P P P
P B B P B P B P P
P P P P P P P P P
8 4
P P P P P P P P
P P P B B P P P
P P B B B B B P
P B B B B B B P
P B P B B B B P
P B P B P B B P
P B B P P B P P
P P P P P P P P
'''

from collections import deque

def check(x,y):
    if x < 0 or x > n -1: return False
    if y < 0 or y > n -1: return False
    return True

def solution(x,y):
    q = deque([[x,y]])
    score = 1
    while q:
        t = q.popleft()
        for i in range(4):
            tx = t[0] + dx[i]
            ty = t[1] + dy[i]
            if check(tx,ty):
                if arr[tx][ty] == 'P':
                    return 1
        else:
            print(x,y)
            for i in range(4):
                tx = t[0] + dx[i]
                ty = t[1] + dy[i]
                while check(tx,ty):
                    if arr[tx][ty] == 'B':
                        score +=1
                    tx += dx[i]
                    ty += dy[i]

    return score


t = int(input())
dx,dy = [0,0,-1,1],[-1,1,0,0]
for tc in range(1, t + 1):
    n,h = map(int,input().split())
    arr = [input().strip().split() for _ in range(n)]
    for i in arr:
        print(i)

    result = 0
    count = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'B':
                height = solution(i,j)
                result += height
                if height >= h:
                    count += 1

    print('#{} {} {}'.format(tc, result,count))