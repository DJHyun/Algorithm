# SW Expert Academy
for _ in range(1, 11):
    test_case = input()
    arr = [list(map(int, input().strip().split(" "))) for _ in range(100)]

    result = float("-inf")
    a = b = 0
    for i in range(100):
        garo = sum(arr[i])

        sero = 0
        for j in range(100):
            if i == j:
                a += arr[i][j]
            sero += arr[j][i]

        b += arr[i][99 - i]
        result = max(result, garo, sero)

    print(f'#{test_case} {max(result, a, b)}')
