import sys

sys.stdin = open("5207_4일차이진탐색.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    a, b = map(int, input().split())
    n_num = list(map(int, input().split()))
    m_num = list(map(int, input().split()))
    n_num.sort()
    cnt = 0

    for i in range(b):
        flag = 0
        l, r = 0, a - 1
        m = (l + r) // 2
        while l <= r:
            check = flag
            if m_num[i] == n_num[m]:
                cnt += 1
                break
            elif m_num[i] > n_num[m]:
                flag = 1
                l = m + 1
                m = (l + r) // 2
            else:
                flag = 2
                r = m - 1
                m = (l + r) // 2

            if check == flag:
                break

    print(f'#{test_case} {cnt}')
