# baekjoon source = "https://www.acmicpc.net/problem/10828"
import sys

T = int(sys.stdin.readline())

stack = [0]*T
tmp = -1
for test_case in range(T):
    
    N = sys.stdin.readline().split()

    if len(N) > 1:
        cmd = N[0]
        number = N[1]
    else:
        cmd = N[0]
    
    if cmd == 'push':
        tmp += 1
        stack[tmp] = number
    elif cmd == 'pop':
        if tmp == -1:
            print(-1)
        else:
            print(stack[tmp])
            stack[tmp] = 0
            tmp -= 1
    elif cmd == 'size':
        print(tmp+1)
    elif cmd == 'empty':
        if tmp == -1:
            print(1)
        else:
            print(0)
    elif cmd == 'top':
        if tmp == -1:
            print(-1)
        else:
            print(stack[tmp])