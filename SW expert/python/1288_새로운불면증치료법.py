# SW Expert Academy
import sys

sys.stdin = open('sample_input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    m = int(input())
    n = m
    tmp = -1
    check = [0] * 10
    result = 1

    while tmp != 9:
        n = m * result
        for i in range(len(str(n))):

            if check[int(str(n)[i])] == 0:
                check[int(str(n)[i])] = 1
                tmp += 1

        result += 1

    print(f'#{test_case} {n}')


