import sys
sys.stdin = open("숫자배열회전.txt", "r")
import copy
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [input().split() for _ in range(N)]
    new_arr = [[0]*N for _ in range(N)]
    new_arr_two = [[0]*N for _ in range(N)]
    new_arr_three = [[0]*N for _ in range(N)]
    result = [['']*3 for _ in range(N)]

    for a in range(3):
        for i in range(N):
            for j in range(N):
                new_arr[i][j] = arr[(N-1)-j][i]
        arr = copy.deepcopy(new_arr)
        for b in range(N):
            result[b][a] = ''.join(arr[b])

    for i in range(N):
        for j in range(N):
            new_arr[i][j] = arr[(N-1)-j][i]
            new_arr_two[i][j] = arr[N-1-i][N-1-j]
            new_arr_three[i][j] = arr[j][N-1-i]
        result[i][0] = ''.join(new_arr[i])
        result[i][1] = ''.join(new_arr_two[i])
        result[i][2] = ''.join(new_arr_three[i])

    # for i in range(N):
    #     for j in range(N):
    #         result[i][0] += arr[(N-1)-j][i]
    #         result[i][1] += arr[N-1-i][N-1-j]
    #         result[i][2] += arr[j][N-1-i]
    #         for a in range(3):
    #             if a == 0:
    #                 result[i][a] += arr[(N-1)-j][i]
    #             elif a == 1:
    #                 result[i][a] += arr[N-1-i][N-1-j]
    #             else:
    #                 result[i][a] += arr[j][N-1-i]

    # for i in range(N):
    #     result[i][0] += arr[0:][0]
    #     result[i][1] += arr[N-1-i][N-1-j]
    #     result[i][2] += arr[j][N-1-i]

    
    print(f'#{test_case}')
    for i in result:
        print(' '.join(i))