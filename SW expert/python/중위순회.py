import sys

sys.stdin = open("중위순회.txt", "r")

def inorder(T):
    if T:
        inorder(arr[T][0])
        print(arr[T][3], end='')
        inorder(arr[T][1])

for test_case in range(1, 11):
    N = int(input())
    arr = [[0] * 4 for _ in range(N + 1)]

    for i in range(N + 1):
        if i != 0:
            list_ = input().split()
            len_ = len(list_)
            if len_ >= 4:
                arr[i][1] = int(list_[3])
                arr[int(list_[3])][2] = int(list_[0])
            if len_ >= 3:
                arr[i][0] = int(list_[2])
                arr[int(list_[2])][2] = int(list_[0])
            arr[i][3] = list_[1]

    print('#{}'.format(test_case), end=' ')
    inorder(1)
    print()
