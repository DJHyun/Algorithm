import sys

sys.stdin = open("금속막대.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    input()
    si = list(map(int, input().split(' ')))
    x, y, result, start, idx = [], [], [], 0, 0
    for s in range(len(si)):
        if s % 2:
            y.append(si[s])
        else:
            x.append(si[s])
    for i in range(len(x)):
        if x[i] not in y:
            start = x[i]
    while len(result) != len(si):
        if len(result) == 0:
            result.append(start)
            result.append(y[x.index(start)])
        else:
            for i in x:
                if i == result[-1]:
                    result.append(i)
                    result.append(y[x.index(i)])
        idx += 1
    print(f'#{test_case} {" ".join(list(map(str, result)))}')
    # ///////////////////////////////////////////////////////////////////////////////////
