# baekjoon source = "https://www.acmicpc.net/problem/1931"
import sys

'''
4
2 5
5 7
1 2
2 3
'''
N = int(sys.stdin.readline())
arr = [0] * N
for i in range(N):
    arr[i] = list(map(int, sys.stdin.readline().split()))
arr = sorted(arr, key=lambda x: (x[1],x[0]))

idx = 0;
cnt = 1
while True:
    a = arr[idx]
    for i in range(idx + 1, N):
        if a[1] <= arr[i][0]:
            cnt += 1
            idx = i
            break
    else:
        print(cnt)
        break
