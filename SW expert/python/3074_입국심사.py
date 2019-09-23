import sys

sys.stdin = open("3074_입국심사.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    im = [int(input()) for _ in range(n)]

    l, r = im[0], im[n - 1] * m
    print(l,r)
    mid = (l + r) // 2

    while l <= r:
        sum_ = 0
        for i in im:
            sum_ += mid // i
            if sum_ >= m:
                break
        print(sum_,mid)
        if sum_ >= m:
            r = mid - 1
            mid = (l + r) // 2
        else:
            l = mid + 1
            mid = (l + r) // 2
    print(f'#{test_case} {l}')
