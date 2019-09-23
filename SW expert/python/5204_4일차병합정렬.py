import sys

sys.stdin = open("5204_4일차병합정렬.txt", "r")

def merge(m):
    global cnt
    len_ = len(m)

    if len_ <= 1:
        return m

    left = merge(m[:len_ // 2])
    right = merge(m[len_ // 2:])

    if left[len(left) - 1] > right[len(right) - 1]:
        cnt += 1

    return merge_sort(left, right)

def merge_sort(m):
    global N, cnt

    len_ = len(m)

    if len_ <= 1:
        return m
    elif len_ == 2:
        result = [0,0]
        left = m[0]
        right = m[1]
        if left > right:
            cnt += 1
            result[0] = right
            result[1] = left
        else:
            result[0] = left
            result[1] = right

        return result
    else:
        left = merge_sort(m[:len_ // 2])
        right = merge_sort(m[len_ // 2:])

        if left[len(left) - 1] > right[len(right) - 1]:
            cnt += 1

        l, r = 0, 0
        l_len = len(left)
        r_len = len(right)
        result, top = [-1] * (l_len + r_len), -1

        while l_len > l and r_len > r:
            if left[l] >= right[r]:
                top += 1
                result[top] = right[r]
                r += 1
            else:
                top += 1
                result[top] = left[l]
                l += 1

        while l_len > l:
            top += 1
            result[top] = left[l]
            l += 1
        while r_len > r:
            top += 1
            result[top] = right[r]
            r += 1

        return result

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = list(map(int, input().split()))
    cnt = 0

    print(f'#{test_case} {merge_sort(arr)[N//2]} {cnt}')