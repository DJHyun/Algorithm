# baekjoon source = "https://www.acmicpc.net/problem/4949"

import sys

while 1:
    st = sys.stdin.readline()

    if st[0] == '.':
        break

    stack = [0] * 100
    top = -1
    flag = False
    check = ['(',')','[',']']
    for i in st:

        if not flag:
            if i in check:
                flag = True

        if i == '(':
            top += 1
            stack[top] = i
        elif i == ')':
            if stack[top] == '(':
                stack[top] = 0
                top -= 1
            else:
                print('no')
                break
        elif i == '[':
            top += 1
            stack[top] = i
        elif i == ']':
            if stack[top] == '[':
                stack[top] = 0
                top -= 1
            else:
                print('no')
                break
    else:
        if flag:
            if stack[top]:
                print('no')
            else:
                print('yes')
        else:
            print('yes')