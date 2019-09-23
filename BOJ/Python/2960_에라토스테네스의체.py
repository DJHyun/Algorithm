# baekjoon source = "https://www.acmicpc.net/problem/2960"
import sys

N, K = map(int,sys.stdin.readline().split())
arr = []

i = 2
j = 1
a = 2
while K != 0:
    if i*j not in arr:
        arr.append(i*j)
        K -= 1
    j += 1
    if i*j > N:
        a += 1
        i = a
        j = 1

print(arr[len(arr)-1])