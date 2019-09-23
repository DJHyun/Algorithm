# SW Expert Academy
for test_case in range(1, 11):
    len_ = int(input())
    arr = list(map(int, input().strip().split(" ")))

    result = 0
    i = 2
    while i < len_-2:
        for j in range(i - 2, i + 3):
            if i == j:
                continue
            if arr[i] <= arr[j]:
                i += 1
                break
        else:
            max_ = 0
            for j in range(i - 2, i + 3):
                if i == j:
                    continue
                max_ = max(max_, arr[j])
            result += arr[i] - max_
            i += 3

    print(f'#{test_case} {result}')
