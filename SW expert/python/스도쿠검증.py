import sys
sys.stdin = open("스도쿠검증.txt", "r")

T = int(input())
test = [list(map(int,input().split())) for _ in range(90)]

case = 0
for test_case in range(1, T + 1):
    arr = [0]*9
    arr_two = [[] for _ in range(9)]
    arr_three = [[] for _ in range(9)]
    idx = 0

    for i in range(case,case+9):
        arr[idx] = test[i]
        idx += 1
    
    idx = 0
    for i in range(9):
        for j in range(case,case+9):
            arr_two[idx].append(test[j][i])
        idx += 1

    idx = 0
    for i in range(case,case+9):
        if i <= case+2:
            pass
        elif i <= case+5:
            idx = 3
        else:
            idx = 6

        for j in range(9):
            if j < 3:
                arr_three[idx].append(test[i][j])
            elif j < 6:
                arr_three[idx+1].append(test[i][j])
            else:
                arr_three[idx+2].append(test[i][j])

    for i in range(9):
        if len(set(arr[i])) != 9:
            print(f'#{test_case} {0}')
            break
        if len(set(arr_two[i])) != 9:
            print(f'#{test_case} {0}')
            break
        if len(set(arr_three[i])) != 9:
            print(f'#{test_case} {0}')
            break
    else:
        print(f'#{test_case} {1}')

    case += 9