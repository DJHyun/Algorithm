# baekjoon source = "https://www.acmicpc.net/problem/1722"
'''
4
1 3

4
2 1 3 2 4
'''

import sys

def fact(num):
    r = 1
    for i in range(2, num + 1):
        r *= i
    return r

n = int(sys.stdin.readline())
m = list(map(int, sys.stdin.readline().split()))
number = list(range(1, n + 1))


if m[0] == 1:
    result = [0]*n
    idx = 0
    while idx < n:
        count = 0
        check = 0
        for i in range(n):
            if number[i] not in result:
                check += fact(n-(idx+1))
                if check >= m[1]:
                    break
                else:
                    count = check
        m[1] -= count
        result[idx] = number[i]
        idx += 1

    print(' '.join(map(str,result)))
else:
    input_number = m[1:]
    visited = [0]*n
    result = 0
    idx = 0
    for i in range(n):
        if input_number[i] == number[idx]:
            visited[number[idx]-1] = 1
            idx += 1
            continue

        if not visited[input_number[i]-1]:
            visited[input_number[i]-1] = 1
            r = visited[0:input_number[i]-1].count(0)
            result += fact(n-(i+1))*r

    print(result+1)

# baekjoon source = "https://www.acmicpc.net/problem/1722"
# import sys
#
# def solution(k,number):
#     global n, cnt,idx
#
#
#     if k == n:
#         print(idx,"번째",' '.join(number))
#         idx += 1
#         cnt += 1
#         if m[0] == 1:
#             pass
#         else:
#             if number == str(m[1])+str(m[2])+str(m[3])+str(m[4]):
#                 print(cnt)
#                 return True
#
#     for i in range(1, n+1):
#         if not visited[i]:
#             visited[i] = 1
#             if solution(k+1, number+str(i)):
#                 break
#             visited[i] = 0
#
# idx = 1
# n = int(sys.stdin.readline())
# m = list(map(int, sys.stdin.readline().split()))
# visited = [0] * (n + 1)
# cnt = 0
#
# solution(0,'')


