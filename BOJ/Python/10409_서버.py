# baekjoon source = "https://www.acmicpc.net/problem/10409"

n,T = map(int,input().split())
arr = list(map(int,input().split()))
cnt = 0
for i in range(n):
    if arr[i] <= T:
        T -= arr[i]
        cnt += 1
    else:
        break

print(cnt)