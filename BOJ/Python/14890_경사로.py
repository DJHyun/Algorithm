# baekjoon source = "https://www.acmicpc.net/problem/14890"

n, l = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(n):
    cnt = 1
    for j in range(n - 1):
        if arr[i][j] == arr[i][j + 1]:
            cnt += 1
        elif arr[i][j] + 1 == arr[i][j + 1]:
            if cnt < l:
                break
            else:
                cnt = 1
        elif arr[i][j] -1 == arr[i][j + 1]:
            if j + l > n-1 or arr[i][j+l] != arr[i][j+1]:
                break
            else:
                cnt = 1-l
        else:
            break
    else:
        result += 1

for i in range(n):
    cnt = 1
    for j in range(n - 1):
        if arr[j][i] == arr[j+1][i]:
            cnt += 1
        elif arr[j][i] + 1 == arr[j+1][i]:
            if cnt < l:
                break
            else:
                cnt = 1
        elif arr[j][i] -1 == arr[j+1][i]:
            if j + l > n-1 or arr[j+l][i] != arr[j+1][i]:
                break
            else:
                cnt = 1-l
        else:
            break
    else:
        result += 1
print(result)