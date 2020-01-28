# SW Expert Academy
import sys

sys.stdin = open("1979_어디에단어가들어갈수있을까.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    for i in range(N):
        for j in range(N - K + 1):
            if arr[i][j] == 1:
                for k in range(K):
                    if arr[i][j + k] != 1:
                        break
                    if k == K - 1:
                        if not (j + k + 1) > N - 1:
                            if arr[i][j + k + 1] == 1:
                                break
                    if k == 0:
                        if j != 0:
                            if arr[i][j + k - 1] == 1:
                                break
                else:
                    result += 1
    for i in range(N):
        for j in range(N - K + 1):
            if arr[j][i] == 1:
                for k in range(K):
                    if arr[j + k][i] != 1:
                        break
                    if k == K - 1:
                        if not (j + k + 1) > N - 1:
                            if arr[j + k + 1][i] == 1:
                                break
                    if k == 0:
                        if j != 0:
                            if arr[j + k - 1][i] == 1:
                                break
                else:
                    result += 1

    print('#{} {}'.format(test_case,result))
