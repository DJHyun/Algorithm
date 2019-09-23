import sys
sys.stdin = open("작업순서.txt", "r")

for test_case in range(1, 11):
    num = list(map(int,input().split()))
    v, e = num[0],num[1]
    g = list(map(int,input().split()))
    x, y,result = [], [],[]
    for i in range(len(g)):
        if i%2:
            y.append(g[i])
        else:
            x.append(g[i])

    i = 0
    while x:
        if x[i] not in y:
            if x[i] not in result:
                result.append(x.pop(i))
                y.pop(i)
                i = 0
            else:
                x.pop(i)
                y.pop(i)
                i = 0
        else:
            i += 1

    for i in range(1,v+1):
        if i not in result:
            result.append(i)
    
    print(f'#{test_case} {" ".join(list(map(str,result))).strip()}')