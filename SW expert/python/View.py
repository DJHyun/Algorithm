# sw_expert_source = "https://www.swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV134DPqAA8CFAYh&categoryId=AV134DPqAA8CFAYh&categoryType=CODE"

import sys
sys.stdin = open("View.txt", "r")
T = int(input())
for test_case in range(1, T+1):
    t = input()
    li = list(map(int,input().split()))
    cnt = 0 
    for i in range(2,len(li)-2):
        if max(li[i-2],li[i-1]) > li[i] or max(li[i+2],li[i+1]) > li[i]:
            continue
        cnt += li[i] - max(max(li[i-2],li[i-1]),max(li[i+2],li[i+1]))
    print(f'#{test_case} {cnt}')




