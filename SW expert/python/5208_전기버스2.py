import sys

sys.stdin = open("5208_전기버스2.txt", "r")

def dfs(n,cnt):
    global result

    if cnt >= result:
        return

    if n >= charge[0]:
        result = min(result,cnt)
        return

    for i in range(len(arr[n])):
        if arr[n][i] not in visited:
            visited.append(arr[n][i])
            dfs(arr[n][i],cnt + 1)
            visited.pop(len(visited)-1)

T = int(input())
for test_case in range(1, T + 1):
    visited = []
    result = 999999999
    charge = list(map(int, input().split()))
    arr = [[] for _ in range(charge[0])]

    for i in range(1,len(charge)):
        for j in range(charge[i]):
            arr[i].append(i+j+1)

    dfs(1,-1)
    print(f'#{test_case} {result}')



