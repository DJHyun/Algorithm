'''
4 5 2 6 1 8 3 7 9
3 7 1 4 2 9 8 6 5
9 8 1 5 7 3 2 4 1
7 3 4 1 6 2 5 6 8
6 2 9 8 4 5 7 1 3
8 1 5 3 9 8 6 2 4
2 9 3 7 5 4 1 8 6
1 4 8 4 3 6 9 5 7
5 6 7 9 8 1 4 3 2
'''

arr = [list(map(int, input().split())) for _ in range(9)]
for i in arr:
    print(i)
check = [[0] * 9 for _ in range(9)]
numbers = []
for i in range(9):
    c = [0] * 10
    for j in range(9):
        if c[arr[i][j]]:
            check[i][j] += 1
            go = c[arr[i][j]]
            check[go[0]][go[1]] += 1
        else:
            c[arr[i][j]] = [i,j]

    c.pop(0)
    if c.count(0) >= 1:
        number = c.index(0)
        numbers.append(number+1)
    c = [0] * 10
    for j in range(9):
        if c[arr[j][i]]:
            check[j][i] += 1
            go = c[arr[j][i]]
            check[go[0]][go[1]] += 1
        else:
            c[arr[j][i]] = [j,i]

for i in range(0,9,3):
    for j in range(0,9,3):
        c = [0]*10
        for a in range(i,i+3):
            for b in range(j,j+3):
                if c[arr[a][b]]:
                    check[a][b] += 1
                    go = c[arr[a][b]]
                    check[go[0]][go[1]] += 1
                else:
                    c[arr[a][b]] = [a,b]

index = 0
for i in range(9):
    for j in range(9):
        if check[i][j] == 3:
            numbers[index] = [i+1,j+1,numbers[index]]
            index +=1
for i in range(index):
    print('#{} {}'.format(i+1, ' '.join(map(str,numbers[i]))))


