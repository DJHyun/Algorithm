# baekjoon source = "https://www.acmicpc.net/problem/2841"
import sys

sys.stdin = open('gitara.in.6','r')

n, p = map(int, sys.stdin.readline().split())
arr = [[0] * p for _ in range(7)]
check = {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1}
index = {1:-1,2:-1,3:-1,4:-1,5:-1,6:-1}

result = 0
for _ in range(n):
    a, b = map(int, sys.stdin.readline().split())

    if check[a] == b:
        continue

    if b > check[a]:
        index[a] += 1
        arr[a][index[a]] = b
        result += 1
        check[a] = b
    else:
        for i in range(index[a], -1, -1):
            if arr[a][i] > b:
                arr[a][i] = 0
                index[a] -= 1
                result += 1
            else:
                break

        check[a] = b
        if arr[a][index[a]] != b:
            index[a] += 1
            arr[a][index[a]] = b
            result += 1
print(result)

