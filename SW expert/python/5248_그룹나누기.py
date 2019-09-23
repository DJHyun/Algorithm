import sys

sys.stdin = open("5248_그룹나누기.txt", "r")

def make_set(x):
    p[x] = x

def find_set(x):
    if x == p[x]:
        return x
    return find_set(p[x])

def union_set(x, y):
    a = find_set(y)
    b = find_set(x)
    p[a] = b
    for i in range(len(p)):
        if p[i] == a:
            p[i] = b

T = int(input())
for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    team_request = list(map(int, input().split()))
    p = [0] * n

    for i in range(n):
        make_set(i)

    for i in range(0, len(team_request), 2):
        union_set(team_request[i] - 1, team_request[i + 1] - 1)

    print(f'#{test_case} {len(set(p))}')
