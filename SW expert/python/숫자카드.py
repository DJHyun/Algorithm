# sw_expert_source = "https://www.swexpertacademy.com/main/learn/course/lectureProblemViewer.do"

import sys
sys.stdin = open("숫자카드.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int,str(input())))
    numbers = []
    result = -1
    cnt = 0
    for i in range(10):
        numbers.append(num.count(i))
    for i in range(len(numbers)):
        if numbers[i] >= result:
            result = numbers[i]
            cnt = i
    print(f'#{test_case} {cnt} {numbers[cnt]}')