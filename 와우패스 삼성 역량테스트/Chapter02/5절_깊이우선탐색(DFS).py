'''
8 1
1 2 1 6 1 8 2 3 2 5 3 4 3 5 4 5 6 7 6 8 -1 -1
'''

def dfs(x):
    for i in range(n+1):
        if arr[x][i] and not visited[i]:
            print(x,i)
            visited[i] = 1
            dfs(i)


n, start = map(int,input().split())
arr = [[0]*(n+1) for _ in range(n+1)]
numbers = list(map(int,input().split()))
visited = [0] * (n+1)
visited[start] = 1
for i in range(0,len(numbers)-1,2):
    arr[numbers[i]][numbers[i+1]] = 1

dfs(start)