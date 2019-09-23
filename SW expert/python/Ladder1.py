import sys
sys.stdin = open("ladder1.txt", "r")

for test_case in range(1, 11):
    input()
    ladder = []
    test = []
    dy = [1,-1,0]

    for i in range(100):
        ladder.append(list(map(int,input().split())))

    for i,v in enumerate(ladder[0]):
        if v == 1:
            test.append(i)

   
    for i in test:
        visited = []
        result = i
        j = 0
        while j <= 99:
            visited.append([j,i])
            if i + dy[0] <= 99 and ladder[j][i+dy[0]] == 1 and [j,i+dy[0]] not in visited:
                i += 1
            elif i + dy[1] >= 0 and ladder[j][i+dy[1]] == 1 and [j,i+dy[1]] not in visited:
                i -= 1
            else:
                j += 1
        if ladder[j-1][i] == 2:
            break
        
    print(f'#{test_case} {result}')
            

