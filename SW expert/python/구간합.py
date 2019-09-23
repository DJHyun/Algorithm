# sw_expert_source = "https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do"

import sys
sys.stdin = open("구간합.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    p = list(map(int,input().split()))
    num = list(map(int,input().split()))
    n,m = p[0],p[1]
    min_result = sum(num[:m])
    max_result = sum(num[:m])

    for i in range(1,n-m+1):
        if min_result > sum(num[i:m+i]):
            min_result = sum(num[i:m+i])
        if max_result < sum(num[i:m+i]):
            max_result = sum(num[i:m+i])

    print(f'#{test_case} {max_result - min_result}')