# baekjoon source = "https://www.acmicpc.net/problem/17136"

def check(x, y, z):
    if x + z > 10: return False
    if y + z > 10: return False
    for a in range(x, x + z):
        for b in range(y, y + z):
            if arr[a][b] != 1:
                return False
    return True

def solution(sum_, k, d):
    global result, result_flag

    if result <= sum_:
        return

    if k == d:
        result = min(result, sum_)
        return

    for i in range(10):
        for j in range(10):
            if arr[i][j] == 1:
                for z in range(5, 0, -1):
                    if check(i, j, z) and visited[z - 1] <= 4:

                        visited[z - 1] += 1
                        kk = 0
                        for a in range(i, i + z):
                            for b in range(j, j + z):
                                arr[a][b] = 2
                                kk += 1

                        solution(sum_ + 1, k + kk, d)

                        visited[z - 1] -= 1
                        for a in range(i, i + z):
                            for b in range(j, j + z):
                                arr[a][b] = 1

                    if z == 1:
                        return

arr = [list(map(int, input().split())) for _ in range(10)]
vv = [[0] * 10 for _ in range(10)]
visited = [0] * 5
result = 99999999
result_flag = True

d = 0
for i in arr:
    d += i.count(1)

solution(0, 0, d)
if result == 99999999:
    print(-1)
else:
    print(result)
