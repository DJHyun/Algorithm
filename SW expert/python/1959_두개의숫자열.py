import sys
sys.stdin = open("1959_두개의숫자열.txt","r")

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    n = list(map(int,input().split()))
    m = list(map(int,input().split()))
    max_ = 0


    if N > M:
        for i in range(N-M+1):
            sum_ = 0
            for j in range(M):
                sum_ += n[i+j] * m[j]
            max_ = max(max_,sum_)
    elif M > N:
        for i in range(M-N+1):
            sum_ = 0
            for j in range(N):
                sum_ += m[i+j] * n[j]
            max_ = max(max_,sum_)
    else:
        sum_ = 0
        for i in range(N):
            sum_ += n[i] * m[i]
        max_ = sum_

    print('#{} {}'.format(test_case,max_))