# baekjoon source = "https://www.acmicpc.net/problem/1874"
import sys

T = int(sys.stdin.readline())
n,result,idx,stack,tmp = [0]*T,[0]*T,-1,[0]*T,-1
answer,ai = [0]*(T*2),-1
for i in range(T):
    n[i] = int(sys.stdin.readline())

ni = 0
for num in n:

    for i in range(ni,num):
        tmp += 1
        stack[tmp] = i+1
        ni += 1
        ai += 1
        answer[ai] = '+'
    
    idx += 1
    result[idx] = stack[tmp]
    stack[tmp] = 0
    tmp -= 1
    ai += 1
    answer[ai] = '-'

    if result[idx] != num:
        print('NO')
        break
else:
    print('\n'.join(answer))



    


