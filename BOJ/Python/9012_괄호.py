# baekjoon source = "https://www.acmicpc.net/problem/1874"
import sys

T = int(sys.stdin.readline())

for test_case in range(T):
    bra = sys.stdin.readline().strip()
    stack,tmp = [0]*len(bra) , -1

    for i in bra:
        if i == '(':
            tmp += 1
            stack[tmp] = i
        else:
            if stack[tmp] == ')' or tmp == -1:
                print('NO')
                break
            else:
                stack[tmp] = 0
                tmp -= 1
    else:
        if tmp != -1:
            print('NO')
        else:
            print('YES')