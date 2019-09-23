# baekjoon source = "https://www.acmicpc.net/problem/2504"
import sys

T = sys.stdin.readline().strip()
stack,top = [0]*len(T), -1
result = [0]*(len(T)+1)
answer,bn = 0,1

for i in T:
    if i == '(':
        top += 1
        stack[top] = i
    elif i =='[':
        top += 1
        stack[top] = i
    elif i == ')':
        if top == -1 or stack[top] != '(':
            print(0)
            break
        else:
            if result[top+1] != 0:
                result[top] += 2*result[top+1]
                result[top+1] = 0
            else:
                result[top] += 2
            stack[top] = 0
            top -= 1
    else:
        if top == -1 or stack[top] != '[':
            print(0)
            break
        else:
            if result[top+1] != 0: 
                result[top] += 3*result[top+1]
                result[top+1] = 0
            else:
                result[top] += 3
            stack[top] = 0
            top -= 1

    if stack[0] == 0:
        for i in range(len(result)):
            if result[i] != 0:
                bn = bn * result[i]
                result[i] = 0
        answer += bn
        bn = 1
else:
    if top == -1:
        print(answer)
    else:
        print(0)