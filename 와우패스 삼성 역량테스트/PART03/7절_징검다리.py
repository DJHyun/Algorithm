'''
4
10
3 2 9 1 4 8 1 2 3 1
6
3 1 2 4 5 7
8
1 2 3 4 5 6 7 8
7
2 0 1 8 0 7 2
'''

t = int(input())
for tc in range(1, t + 1):
    n = int(input())
    arr = list(map(int, input().split()))

    check = [float('inf') for _ in range(n + 1)]
    for i in range(3):
        check[i] = arr[i]

    for i in range(3, n + 1):
        if i < n:
            for j in range(3):
                check[i] = min(check[i], check[i - 3 + j] + arr[i])
        else:
            for j in range(3):
                check[i] = min(check[i], check[i - 3 + j])

    print(check[n])

