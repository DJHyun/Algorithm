# baekjoon source = "https://www.acmicpc.net/problem/2304"
'''
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6

3
4 6
8 10
2 4

3
2 10
4 6
8 4

5
2 10
4 5
6 5
8 5
10 10

4
2 5
4 5
8 5
6 5

3
4 4
6 2
2 2

1
2 5

'''
import sys

N = int(sys.stdin.readline())
arr = [0]*N
result = 0
for i in range(N):
    L, H = map(int,sys.stdin.readline().split())
    arr[i] = (H,L)

arr = sorted(arr, key=lambda x: x[1])
max_ = arr[0]

for i in range(1,N):
    if arr[i][0] > max_[0]:
        result += abs(arr[i][1] - max_[1]) * max_[0]
        max_ = arr[i]
    else:
        if arr[i] == max(arr[i:]):
            result += (abs(arr[i][1] - max_[1]) * arr[i][0] + abs(max_[0] - arr[i][0]))
            max_ = arr[i]

result += arr[N-1][0]

print(result)
