# baekjoon source = "https://www.acmicpc.net/problem/5430"
import sys

T = int(sys.stdin.readline())

for test_case in range(T):
    meto = sys.stdin.readline().strip()
    count = int(sys.stdin.readline())
    len_meto = len(meto)

    first = -1
    c = sys.stdin.readline()
    len_c = len(c)
    c = c[1:len_c - 2].split(',')
    rear = count - 1

    if count == 0:
        if 'D' in meto:
            print('error')
        else:
            print('[]')
    else:
        flag = True
        for i in range(len_meto):
            if meto[i] == 'D':
                if first == rear:
                    print('error')
                    break
                if flag:
                    first += 1
                    c[first] = 0
                else:
                    c[rear] = 0
                    rear -= 1
            else:
                if flag:
                    flag = False
                else:
                    flag = True
        else:
            print('[', end='')
            if flag:
                for j in range(first + 1, rear + 1):
                    if j != rear:
                        print(c[j] + ',', end='')
                    else:
                        print(c[j], end='')
                print(']')
            else:
                for j in range(rear, first, -1):
                    if j != first+1:
                        print(c[j] + ',', end='')
                    else:
                        print(c[j], end='')
                print(']')
