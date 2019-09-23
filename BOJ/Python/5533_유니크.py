# baekjoon source = "https://www.acmicpc.net/problem/5533"
import copy
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

# for i in range(n):
#     check = [1, 1, 1]
#     for j in range(n):
#         if i != j:
#             for z in range(3):
#                 if check[z]:
#                     if arr[i][z] == arr[j][z]:
#                         check[z] = 0
#     result = 0
#     for j in range(3):
#         result += (arr[i][j] * check[j])
#     print(result)
#

score = copy.deepcopy(arr)
for i in range(3):
    for j in range(n):
        for z in range(j+1,n):
            if arr[z][i] == arr[j][i]:
                score[z][i] = 0
                score[j][i] = 0


for i in score:
    print(sum(i))