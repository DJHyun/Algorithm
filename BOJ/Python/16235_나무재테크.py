# baekjoon source = "https://www.acmicpc.net/problem/16235"
'''
5 2 1
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

5 2 7
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 3 2 3 2
2 1 3
3 2 3

10 1 1000
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
100 100 100 100 100 100 100 100 100 100
1 1 1

2 1 2
0 100
0 0
1 2 5
'''

def check(x, y):
    global n
    if x < 0 or x > n - 1: return False
    if y < 0 or y > n - 1: return False
    return True

n, m, k = map(int, input().split())
arr = [[[5] for _ in range(n)] * n for _ in range(n)]
for i in range(n):
    for j in range(n):
        arr[i][j] += [0] * 200
add_arr = [list(map(int, input().split())) for _ in range(n)]
result = 0

for i in range(m):
    tree_input = list(map(int, input().split()))
    tree_input[0] -= 1
    tree_input[1] -= 1
    arr[tree_input[0]][tree_input[1]][tree_input[2]] += 1
    result += 1

dx, dy = [-1, -1, -1, 0, 0, 1, 1, 1], [-1, 0, 1, -1, 1, -1, 0, 1]

idx = 0
while idx < k:
    # 봄
    for i in range(n):
        for j in range(n):

            flag = True
            tree = [0] * 201
            # 봄
            for z in range(1, 201):
                for a in range(arr[i][j][z]):
                    if flag:
                        if arr[i][j][0] >= z:
                            arr[i][j][0] -= z
                            arr[i][j][z] -= 1
                            tree[z + 1] += 1
                        else:
                            flag = False
                            arr[i][j][0] += z // 2
                            arr[i][j][z] -= 1
                            result -= 1
                    else:
                        tree[0] += z // 2
                        arr[i][j][z] -= 1
                        result -= 1
            # 여름
            for z in range(201):
                arr[i][j][z] += tree[z]

    for i in range(n):
        for j in range(n):

            # 가을
            for z in range(1, 201):
                if not z % 5:
                    for a in range(arr[i][j][z]):
                        for b in range(8):
                            tx = i + dx[b]
                            ty = j + dy[b]
                            if check(tx, ty):
                                arr[tx][ty][1] += 1
                                result += 1

            # 겨울
            arr[i][j][0] += add_arr[i][j]

    idx += 1
    for i in arr:
        print(i)
    print()
print(result)
