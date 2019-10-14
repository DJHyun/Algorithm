# baekjoon source = "https://www.acmicpc.net/problem/1712"
import sys
arr = list(map(int, sys.stdin.readline().split()))
left = 1
right = 2100000000
mid = (right + left) // 2
if arr[1] >= arr[2]:
    print(-1)
else:
    while True:
        if left > right:
            print(mid+1)
            break

        if arr[0] + arr[1] * mid < arr[2] * mid:
            right = mid - 1
        else:
            left = mid + 1
        mid = (right + left) // 2
