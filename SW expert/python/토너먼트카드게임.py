import sys
sys.stdin = open("토너먼트카드게임.txt", "r")

def merge(arr):
    len_ = len(arr)
    if len_ <= 1:
        return arr
    if len_%2:
        left = merge(arr[:(len_//2)+1])
        right = merge(arr[(len_//2)+1:])
    else:
        left = merge(arr[:(len_//2)])
        right = merge(arr[(len_//2):])

    return solution(left, right)

def solution(left, right):
    result = []
    if int(left[0][0]) == 1:
        if int(right[0][0]) == 2:
            result = right
        elif int(right[0][0]) == 3:
            result = left
        elif int(right[0][0]) == 1:
            if int(left[0][1:]) > int(right[0][1:]):
                result = right
            else:
                result = left

    elif int(left[0][0]) == 2:
        if int(right[0][0]) == 3:
            result = right
        elif int(right[0][0]) == 1:
            result = left
        elif int(right[0][0]) == 2:
            if int(left[0][1:]) > int(right[0][1:]):
                result = right
            else:
                result = left

    elif int(left[0][0]) == 3:
        if int(right[0][0]) == 1:
            result = right
        elif int(right[0][0]) == 2:
            result = left
        elif int(right[0][0]) == 3:
            if int(left[0][1:]) > int(right[0][1:]):
                result = right
            else:
                result = left
    return result

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    stu = input().split()
    for i in range(N):
        stu[i] = stu[i]+f'{i+1}'

    print(f'#{test_case} {int(merge(stu)[0][1:])}')