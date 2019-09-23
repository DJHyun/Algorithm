import sys

sys.stdin = open("사칙연산.txt", "r")


def postorder(T):
    global top
    check = ['-', '+', '/', '*']
    if T:
        postorder(arr[T][0])
        postorder(arr[T][1])

        if arr[T][3] not in check:
            top += 1
            result[top] = int(arr[T][3])
        else:
            if arr[T][3] == '-':
                result[top - 1] -= result[top]
                result[top] = 0
                top -= 1
            elif arr[T][3] == '+':
                result[top - 1] += result[top]
                result[top] = 0
                top -= 1
            elif arr[T][3] == '*':
                result[top - 1] *= result[top]
                result[top] = 0
                top -= 1
            else:
                result[top - 1] /= result[top]
                result[top] = 0
                top -= 1


for test_case in range(1, 11):
    N = int(input())
    arr = [[0] * 4 for _ in range(N + 1)]
    result, top = [0] * (N//2), -1

    for i in range(N):
        list_ = input().split()
        if len(list_) >= 4:
            arr[int(list_[3])][2] = int(list_[0])
            arr[i + 1][1] = int(list_[3])
        if len(list_) >= 3:
            arr[int(list_[2])][2] = int(list_[0])
            arr[i + 1][0] = int(list_[2])
        arr[i + 1][3] = list_[1]

    postorder(1)
    print('#{} {}'.format(test_case, int(result[0])))
