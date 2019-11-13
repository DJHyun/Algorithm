# baekjoon source = "https://www.acmicpc.net/problem/9019"

import sys
from collections import deque

def solution(x):
    global b

    q = deque([[x, []]])
    visited[x] = 1
    while q:
        t = q.popleft()
        number = t[0]
        for i in range(4):
            if i == 0:
                new_number = (number * 2) % 10000
                if new_number == b:
                    return t[1] + ['D']
                if not visited[new_number]:
                    visited[new_number] = 1
                    q.append([new_number, t[1]+['D']])
            elif i == 1:
                if number == 0:
                    new_number = 9999
                else:
                    new_number = number - 1
                if new_number == b:
                    return t[1] + ['S']
                if not visited[new_number]:
                    visited[new_number] = 1
                    q.append([new_number, t[1] + ['S']])
            elif i == 2:
                n = str(number)
                zero = 4-len(n)
                n = '0'*zero+n
                new_number = n[1]+n[2]+n[3]+n[0]
                new_number = int(new_number)
                if new_number == b:
                    return t[1] +['L']
                if not visited[new_number]:
                    visited[new_number] = 1
                    q.append([new_number,t[1]+['L']])
            else:
                n = str(number)
                zero = 4-len(n)
                n = '0'*zero+n
                new_number = n[3]+n[0]+n[1]+n[2]
                new_number = int(new_number)
                if new_number == b:
                    return t[1]+['R']
                if not visited[new_number]:
                    visited[new_number] = 1
                    q.append([new_number, t[1]+['R']])

t = int(sys.stdin.readline())
for _ in range(t):
    a, b = map(int, sys.stdin.readline().split())
    visited = [0] * 10001

    print(''.join(solution(a)))
