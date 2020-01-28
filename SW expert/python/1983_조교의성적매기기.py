# SW Expert Academy
import sys

sys.stdin = open('input (19).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    arr = [0] * n
    gogo = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']

    for i in range(n):
        grades = list(map(int, input().split()))
        arr[i] = [grades[0] * 0.35 + grades[1] * 0.45 + grades[2] * 0.2, i + 1]

    arr = sorted(arr, key=lambda x: (x[0], x[1]), reverse=True)

    # print(n, m)
    # for i in arr:
    #     print(i)
    # print()

    idx = 0
    for k,i in enumerate(arr):
        if i[1] == m:
           idx = k


    print(f'#{test_case} {gogo[idx//(n//10)]}')
