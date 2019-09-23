# baekjoon source = "https://www.acmicpc.net/problem/6064"
import sys

T = int(sys.stdin.readline())

for _ in range(T):
    M,N,x,y = map(int,sys.stdin.readline().split())
    
    if M > N:
        min_year = N
        min_ = y
        check = x
    else:
        min_year = M
        min_ = x
        check = y
    sub_year = abs(M-N)

    c = min_
    cnt = min_

    while c != check:
        cnt += min_year

        if c - sub_year <= 0:
            c = c - sub_year +max(M,N)
        else:
            c = c - sub_year

        if c == min_:
            print(-1)
            break
    else:
        print(cnt)