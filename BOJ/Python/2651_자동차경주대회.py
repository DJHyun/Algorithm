# baekjoon source = "https://www.acmicpc.net/problem/2651"
'''
140
5
100 30 100 40 50 60
5 2 7 11 7

400
5
100 30 100 40 50 60
5 10 4 11 7

110
3
100 20 30 100
1 2 3

2
100
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

'''

import sys

def solution(index, check, result, go):
    global n, d, c, re, time

    for i in range(index + 1, n + 2):
        check += arr[i]
        if d >= check:
            if i == n + 1:
                if c > result:
                    c = result
                    re = go[:]

            if result + time[i] < visited[i]:
                visited[i] = result + time[i]
                solution(i, 0, result + time[i], go + [str(i)])
        else:
            break

d = int(sys.stdin.readline())
n = int(sys.stdin.readline())
arr = [0]
arr += list(map(int, sys.stdin.readline().strip().split()))
time = [0]
time += list(map(int, sys.stdin.readline().strip().split()))
time += [0]
visited = [float('inf')] * (n + 2)
c = float('inf')
re = 0

if d >= sum(arr):
    sys.stdout.write(str(re)+'\n')
    sys.stdout.write(str(re))
else:
    solution(0, 0, 0, [])
    print(c)
    print(len(re))
    print(' '.join(re))
