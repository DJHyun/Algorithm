'''
4
1324327277847
31055718578107
437156809571890578147849532
54395745907898790879656
'''

t = int(input())
for tc in range(1, t + 1):
    numbers = list(map(int, input()))

    check = [0] * 10
    for i in range(len(numbers)):
        check[numbers[i]] += 1
    for i in range(len(check)):
        if not check[i]:
            check[i] = -1
    score = [[] for _ in range(10)]
    index = 0
    result = 0
    max_ = 0
    for i in range(len(numbers)):
        if check[numbers[i]] != -1:
            max_ = max(max_, check[numbers[i]])
            for j in range(check[numbers[i]]):
                score[index].append(numbers[i])
            check[numbers[i]] = -1
            index += 1

    for i in range(len(score)):
        if len(score[i]) < max_:
            for j in range(max_ - len(score[i])):
                score[i].append(-1)

    for i in range(max_):
        s = ''
        for j in range(len(score)):
            if score[j][i] == -1:
                continue
            s += str(score[j][i])
        result += int(s)
    print('#{} {}'.format(tc, result))
