# baekjoon source = "https://www.acmicpc.net/problem/15686"
import itertools

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
chicken = []

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            chicken.append([i, j])


result = 9999999999

cnt = 9999999
for z in itertools.combinations(chicken, m):
    ca = 0
    for a in range(n):
        for b in range(n):
            if arr[a][b] == 1:
                cz = []
                for c in z:
                    cz.append(abs(c[0] - a) + abs(c[1] - b))
                cz = min(cz)
                ca += cz
    result = min(result, ca)

print(result)
