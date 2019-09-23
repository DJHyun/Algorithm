# baekjoon source = "https://www.acmicpc.net/problem/1024"
import sys

N, L = map(int,sys.stdin.readline().split())
flag = True

while L <= 100:
    n = N // L
    result, top = [-1]*L, -1
    top += 1
    result[top] = n

    if L%2:
        ti, fi = 1, 1
        for i in range(1,L):
            top += 1
            if i % 2:
                result[top] = n + ti
                ti += 1
            else:
                if n - fi < 0:
                    break
                result[top] = n - fi
                fi += 1
        if sum(result) == N:
            print(' '.join(list(map(str,sorted(result)))))
            flag = False
            break
        else:
            L += 1 
    else:
        ti, fi = 1, 1
        for i in range(1,L):
            top += 1
            if i%2:
                result[top] = n + ti
                ti += 1
            else:
                if n - fi < 0:
                    break
                result[top] = n - fi
                fi += 1
        if sum(result) == N:
            print(' '.join(list(map(str,sorted(result)))))
            flag = False
            break
        else:
            L += 1 

if flag:
    print(-1)