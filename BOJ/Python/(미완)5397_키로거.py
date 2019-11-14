# baekjoon source = "https://www.acmicpc.net/problem/5397"

import sys

t = int(sys.stdin.readline())
for _ in range(t):
    input_ = sys.stdin.readline().strip()
    q = []
    index = 0

    for i in input_:
        if i == '<':
            if index == 0:
                continue
            index -= 1
        elif i == '>':
            if index == len(q):
                continue
            index += 1
        elif i == '-':
            if index == 0:
                continue
            index -= 1
            ne = q[:index]+q[index+1:]
            q = ne[:]
        else:
            q.insert(index,i)
            index += 1

    sys.stdout.write(''.join(q)+'\n')
