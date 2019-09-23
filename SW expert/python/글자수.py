import sys
sys.stdin = open("글자수.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    str1 = input()
    str2 = input()
    result, my_max = {}, 0

    for i in str1:
        result[i] = 0

    for i in str2:
        if i in result:
            result[i] += 1

    for i in result.values():
        if i > my_max:
            my_max = i

    print(f'#{test_case} {my_max}')