# baekjoon source = "https://www.acmicpc.net/problem/10845"
import sys

def my_push(x):
    q.append(x)

def my_pop():
    if q:
        print(q.pop(0))
    else:
        print(-1)

def my_size():
    print(len(q))

def my_empty():
    if q:
        print(0)
    else:
        print(1)

def my_front():
    if q:
        print(q[0])
    else:
        print(-1)

def my_back():
    if q:
        print(q[len(q)-1])
    else:
        print(-1)

N = int(sys.stdin.readline())
q = []

for i in range(N):
    inp = sys.stdin.readline().split()
    if len(inp) == 1:
        if inp[0] == 'pop':
            my_pop()
        elif inp[0] == 'size':
            my_size()
        elif inp[0] == 'empty':
            my_empty()
        elif inp[0] == 'front':
            my_front()
        else:
            my_back()
    else:
        my_push(int(inp[1]))


