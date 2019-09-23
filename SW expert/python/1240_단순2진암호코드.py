import sys

sys.stdin = open("1240_단순2진암호코드.txt", "r")


def solution(num):
    odd = even = 0

    for i in range(len(num) - 1):
        if i % 2:
            even += num[i]
        else:
            odd += num[i]
    if (odd * 3 + even + num[7]) % 10:
        return 0
    else:
        return odd + even + num[7]


T = int(sys.stdin.readline())
for test_case in range(1, T + 1):
    N, M = map(int, sys.stdin.readline().split())
    arr = [list(sys.stdin.readline().strip()) for _ in range(N)]
    check = ['0001101', '0011001', '0010011', '0111101', '0100011', '0110001', '0101111',
             '0111011', '0110111', '0001011']
    number, top = [0] * 8, -1

    for i in arr:
        if i.count('1') >= 3:
            arr = i
            break
    x = arr.index('1')

    if x >= 3 and '1' not in arr[x - 3 + 57:]:
        x -= 3
        while top != 7:
            if ''.join(arr[x:x + 7]) in check:
                top += 1
                number[top] = check.index(''.join(arr[x:x + 7]))
                x += 7
            else:
                x += 1
    elif x >= 2 and '1' not in arr[x - 2 + 57:]:
        x -= 2
        while top != 7:
            if ''.join(arr[x:x + 7]) in check:
                top += 1
                number[top] = check.index(''.join(arr[x:x + 7]))
                x += 7
            else:
                x += 1
    else:
        x -= 1
        while top != 7:
            if ''.join(arr[x:x + 7]) in check:
                top += 1
                number[top] = check.index(''.join(arr[x:x + 7]))
                x += 7
            else:
                x += 1

    print(f'#{test_case} {solution(number)}')
