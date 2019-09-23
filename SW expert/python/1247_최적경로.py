import sys

sys.stdin = open("1247_최적경로.txt", "r")

def solution(a, k, check, sum_):
    global total

    c = [0] * check

    if k == check:
        sum_ += dis(arr[0], arr[a[k] + 2])
        total = min(total, sum_)
    else:
        k += 1
        ncandi = candi(a, k, check, c)
        for i in range(ncandi):
            a[k] = c[i]
            if sum_ >= total:
                break
            if k == 1:
                solution(a, k, check, sum_ + dis(arr[1], arr[a[k] + 2]))
            else:
                solution(a, k, check, sum_ + dis(arr[a[k - 1] + 2], arr[a[k] + 2]))

def candi(a, k, check, c):
    in_perm = [False] * check

    for i in range(1, k):
        in_perm[a[i]] = True

    ncandi = 0
    for i in range(check):
        if not in_perm[i]:
            c[ncandi] = i
            ncandi += 1

    return ncandi

def dis(x, y):
    return abs(x[0] - y[0]) + abs(x[1] - y[1])

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int, input().split()))
    arr = []
    for i in range(0, len(num), 2):
        arr.append([num[i], num[i + 1]])

    a = [0] * (N + 1)
    total = 99999999
    for i in arr:
        print(i)
    print()
    solution(a, 0, N, 0)
    print(f'#{test_case} {total}')
