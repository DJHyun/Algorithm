import sys

sys.stdin = open("subtree.txt", "r")

def result(T):
    global cnt
    if T:
        cnt += 1
        result(arr[T][0])
        result(arr[T][1])

    return cnt

T = int(input())
for test_case in range(1, T + 1):
    E, N = map(int, input().split())
    node = list(map(int, input().split()))
    arr = [[0] * 3 for _ in range(max(node) + 1)]
    cnt = 0

    for i in range(0, E * 2, 2):
        if arr[node[i]][0] == 0:
            arr[node[i]][0] = node[i + 1]
        else:
            arr[node[i]][1] = node[i + 1]
        arr[node[i + 1]][2] = node[i]

    print('#{} {}'.format(test_case, result(N)))
