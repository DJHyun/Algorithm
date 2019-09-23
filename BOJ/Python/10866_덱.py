# baekjoon source = "https://www.acmicpc.net/problem/10866"
import sys
from collections import deque

d = deque()

print(dir(d))
N = int(sys.stdin.readline())
q = []

for _ in range(N):
    cmd = sys.stdin.readline().split()

    if len(cmd) == 2:
        if cmd[0] == 'push_back':
            q.append(cmd[1])
        else:
            q.insert(0, cmd[1])
    else:
        if cmd[0] == 'pop_front':
            if len(q) == 0:
                print('-1')
            else:
                print(q.pop(0))
        elif cmd[0] == 'pop_back':
            if len(q) == 0:
                print('-1')
            else:
                print(q.pop(len(q)-1))
        elif cmd[0] == 'size':
            print(len(q))
        elif cmd[0] == 'empty':
            if q:
                print('0')
            else:
                print('1')
        elif cmd[0] == 'front':
            if q:
                print(q[0])
            else:
                print('-1')
        else:
            if q:
                print(q[len(q)-1])
            else:
                print('-1')




