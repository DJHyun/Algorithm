import sys

sys.stdin = open("2383_점심식사시간.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    man = []
    stair = []
    time = []


    for i in arr:
        print(i)
    print()

    for i in range(n):
        for j in range(n):
            if arr[i][j] == 1:
                man.append([i,j])
            elif arr[i][j] != 0:
                time.append(arr[i][j])
                stair.append([i,j])

    total = [[0,0] for _ in range(len(man))]

    for i in range(len(man)):
        for j in range(len(stair)):
            total[i][j] = abs(stair[j][0] - man[i][0])+abs(stair[j][1] - man[i][1])

    for i in range(len(man)):
        for j in range(len(time)):
            man[i][j] = total[i][j]+time[j]+1


    print(man,stair)
    print(total)
    print(time)
    print()
