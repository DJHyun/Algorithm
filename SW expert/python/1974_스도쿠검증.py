# SW Expert Academy
import sys

sys.stdin = open('input (22).txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    result = 0
    flag = True

    for i in arr:
        if len(set(i)) != 9:
            flag = False
            break
    else:
        for a in range(9):
            if flag:
                check = [0] * 9
                for b in range(9):
                    if not check[arr[b][a] - 1]:
                        check[arr[b][a] - 1] = 1
                    else:
                        flag = False
                        break
            else:
                break
        else:
            for i in range(0, 9, 3):
                for j in range(0, 9, 3):
                    check = [0] * 9
                    for a in range(i, i + 3):
                        for b in range(j, j + 3):
                            if not check[arr[b][a] - 1]:
                                check[arr[b][a] - 1] = 1
                            else:
                                flag = False
                                break

    if flag:
        result = 1

    print(f'#{test_case} {result}')
