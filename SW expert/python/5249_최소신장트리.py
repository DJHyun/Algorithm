import sys

sys.stdin = open("5249_최소신장트리.txt", "r")

def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]:
        return x
    else:
        return find_set(p[x])

def union(x,y):
    p[find_set(y)] = find_set(x)

def solution():
    global v

    for i in range(v+1):
        make_set(i)

    for i in range(e):
        v = arr[i][0]
        u = arr[i][1]
        if find_set(v) != find_set(u):
            union(v,u)
            a.append(arr[i])

    return a

T = int(input())
for test_case in range(1, T + 1):
    v, e = map(int, input().split())
    visited = [0] * (v+1)
    arr = [[0]*3 for _ in range(e)]
    p = [0] * (v+1)
    a = []
    result = 0

    for i in range(e):
        num = list(map(int, input().split()))
        arr[i][0] = num[0]
        arr[i][1] = num[1]
        arr[i][2] = num[2]

    arr = sorted(arr, key=lambda x: x[2])

    solution()
    for i in a:
        result += i[2]
    print(f'#{test_case} {result}')



