# baekjoon source = "https://www.acmicpc.net/problem/2660"
'''
5
1 2
2 3
3 4
4 5
2 4
5 3
-1 -1

2
1 2
-1 -1

3
1 2
2 3
-1 -1

5
1 2
2 3
3 4
4 5
-1 -1

6
1 2
2 3
3 4
4 5
5 6
2 4
2 5
-1 -1
'''
import sys

def bfs(i):
    tp = []
    visited = []
    tp.append(i)
    visited.append(i)
    idx = -1

    while tp:
        p = tp[:]
        while p:
            t = p.pop(0)
            tp.pop(0)
            for a in range(1, N + 1):
                if a not in visited and arr[t][a] == 1:
                    tp.append(a)
                    visited.append(a)
        
        idx += 1

    return idx
                

N = int(sys.stdin.readline())
arr = [[0] * (N + 1) for _ in range(N + 1)]
result = [0]*(N + 1)


while True:
    a, b = map(int, sys.stdin.readline().split())
    if a == -1 and b == -1:
        break

    arr[a][a] = 1
    arr[b][b] = 1
    arr[a][b] = 1
    arr[b][a] = 1

for i in range(1, N + 1):
    result[i] = bfs(i)
            
print(min(result[1:]), result.count(min(result[1:])))
for i in range(1,N + 1):
    if result[i] == min(result[1:]):
        print(i, end=' ')
