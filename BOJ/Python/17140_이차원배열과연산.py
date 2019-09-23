# baekjoon source = "https://www.acmicpc.net/problem/17140"

'''
1 2 3
1 2 1
2 1 3
3 3 3

2
'''
r, c, k = map(int, input().split())
r -= 1
c -= 1
arr = [list(map(int, input().split())) for _ in range(3)]
garo = 3
sero = 3
result = 0

if r < garo and c < sero:
    k_re = arr[r][c]
else:
    k_re = 0

while k_re != k:

    if result > 100:
        result = -1
        break

    result += 1

    if garo >= sero:
        check = [{} for _ in range(garo)]
        len_ = 0
        for i in range(garo):
            count = 0
            for j in range(sero):
                if arr[i][j] == 0:
                    continue
                if arr[i][j] not in check[i]:
                    check[i][arr[i][j]] = 1
                else:
                    check[i][arr[i][j]] += 1
                count +=2
                if count > 100:
                    break
            check[i] = sorted(check[i].items(), key=lambda x: (x[1], x[0]))
            len_ = max(len_, len(check[i]) * 2)

        new_arr = [[0] * len_ for _ in range(garo)]

        for i in range(garo):
            new_idx = 0
            for j in range(len(check[i])):
                new_arr[i][new_idx] = check[i][j][0]
                new_arr[i][new_idx + 1] = check[i][j][1]
                new_idx += 2

        # for i in new_arr:
        #     print(i)
        # print()

        arr = new_arr
        sero = len_
    else:

        check = [{} for _ in range(sero)]
        len_ = 0

        for i in range(sero):
            count = 0
            for j in range(garo):
                if arr[j][i] == 0:
                    continue
                if arr[j][i] not in check[i]:
                    check[i][arr[j][i]] = 1
                else:
                    check[i][arr[j][i]] += 1
                count += 2
                if count > 100:
                    break
            check[i] = sorted(check[i].items(), key=lambda x: (x[1], x[0]))
            len_ = max(len_, len(check[i]) * 2)

        new_arr = [[0] * sero for _ in range(len_)]
        for i in range(sero):
            new_idx = 0
            for j in range(len(check[i])):
                new_arr[new_idx][i] = check[i][j][0]
                new_arr[new_idx + 1][i] = check[i][j][1]
                new_idx += 2

        # for i in new_arr:
        #     print(i)
        # print()

        arr = new_arr
        garo = len_

    if r < garo and c < sero:
        k_re = arr[r][c]
print(result)
