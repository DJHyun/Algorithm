'''
4
HELLOWORLDSAQ
NOPAINAGAIN
HAPPYHOLIDAY
MERRYCHRISTMASANDHAPPYNEWYEAR
'''

t = int(input())
for tc in range(t):
    s = input().strip()
    check = [[]]
    al = []
    for i in range(65,91):
        al.append(chr(i))
    index = 0
    c = 0
    go = 0
    while go < len(s):
        if go > 0:
            if s[go] == s[go-1]:
                go+=1
                continue
        if index < c:
            check[c].append(s[go])
            index += 1
        else:
            check.append([])
            check[c].append(s[go])
            c += 1
            index = 0
        go += 1
    for i in range(len(check) - len(check[len(check)-1])):
        check[len(check)-1].append(al[i])

    result = [[],[]]
    for i in range(len(check)):
        result[0].append(check[i][0])
        result[1].append(check[i][i])

    print('#{}'.format(tc+1),end=' ')
    for i in range(2):
        print(''.join(result[i]),end=' ')
    print()