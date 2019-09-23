# SW Expert Academy


for test_case in range(1, 11):
    n = int(input())
    arr = list(map(int, input().strip().split(" ")))

    index = 0
    while index < n:
        max_ = max(arr)
        min_ = min(arr)
        arr[arr.index(max_)] -= 1
        arr[arr.index(min_)] += 1
        index += 1
    print(f'#{test_case} {max(arr) - min(arr)}')


# for test_case in range(1, 11):
#     n = int(input())
#     arr = list(map(int, input().strip().split(" ")))
#     index = 0
#
#     while index < n:
#         check = [0, float('INF'), 0, float('-INF')]
#         for i, v in enumerate(arr):
#             if v > check[3]:
#                 check[2] = i
#                 check[3] = v
#
#             if v < check[1]:
#                 check[0] = i
#                 check[1] = v
#
#         arr[check[0]] += 1
#         arr[check[2]] -= 1
#
#         index += 1
#
#     print(f'#{test_case} {max(arr) - min(arr)}')


