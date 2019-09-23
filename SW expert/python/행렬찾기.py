import sys

sys.stdin = open("행렬찾기.txt", "r")

T = int(input())
 
for test_case in range(1, T + 1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    result = []
    check = 0
 
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 0:
                if check != 0:
                    for z in range(i+1,n):
                        if arr[z][j-1] == 0:
                            result.append([z-i,check])
                            check = 0
                            break
                        else:
                            for b in range(check):
                                arr[z][j-1-b] = 0
            else:
                check += 1
                arr[i][j] = 0
 
 
    result = sorted(result, key=lambda x:(x[0]*x[1],x[0]))
    pr, top = [0]*(len(result)*2), -1
    for i in result:
        for j in i:
           top += 1
           pr[top] = str(j) 
 
    print(f'#{test_case} {len(result)} {" ".join(pr)}')
    
        