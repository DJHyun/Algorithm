import sys

sys.stdin = open('input (16).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    result = [[0] * n for i in range(n)]
    result[0][0] = 1

    # for i in result:
    #     print(i)
    # print()

    for i in range(1, n):
        for j in range(n):
            if j == 0:
                result[i][j] = result[i - 1][j]
            else:
                result[i][j] = result[i - 1][j - 1] + result[i - 1][j]

    print(f'#{test_case}')
    for i in result:
        print(' '.join(map(str, i)).strip(' 0'))
