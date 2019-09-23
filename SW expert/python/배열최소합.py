import sys
sys.stdin = open("배열최소합.txt", "r")

def backtrack(a, k, input,sum_num):
    global sum_,N
    c = [0] * N

    if k == input :
        print(a)
        if sum_>sum_num:
            sum_=sum_num
    else:
        if sum_num < sum_:
            k += 1
            ncandi = construct(a, k, input, c)
            for i in range(ncandi):
                a[k] = c[i]
                backtrack(a, k, input,sum_num+arr[a[k]][k-1])

def construct(a, k, input, c):
    global ncandi
    in_perm = [False]*input

    for i in range(1,k):
        in_perm[a[i]] = True
    
    ncandi = 0

    for i in range(0, input):
        if in_perm[i] == False:
            c[ncandi] = i
            ncandi += 1

    return ncandi

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    ncandi = N
    a = [0] * (N+1)
    sum_ = 9999
    arr = [list(map(int, input().split())) for x in range(N)]

    backtrack(a, 0, N, 0)

    print(f'#{test_case} {sum_}')