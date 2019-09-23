import sys

sys.stdin = open("4366_정식이의은행업무.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    two = list(input())
    three = list(input())
    len_two = len(two)
    len_three = len(three)

    two_check = []
    three_check = []

    for i in range(len_two):
        if two[i] == '1':
            two[i] = '0'
            val = 0
            for j in range(len_two - 1, -1, -1):
                val += int(two[j]) * (2 ** (len_two - 1 - j))
            two_check.append(val)
            two[i] = '1'
        else:
            two[i] = '1'
            val = 0
            for j in range(len_two - 1, -1, -1):
                val += int(two[j]) * (2 ** (len_two - 1 - j))
            two_check.append(val)
            two[i] = '0'

    for i in range(len_three):
        if three[i] == '1':
            three[i] = '0'
            val = 0
            for j in range(len_three - 1, -1, -1):
                val += int(three[j]) * (3 ** (len_three - 1 - j))
                three_check.append(val)
            three[i] = '2'
            val = 0
            for j in range(len_three - 1, -1, -1):
                val += int(three[j]) * (3 ** (len_three - 1 - j))
                three_check.append(val)
            three[i] = '1'
        elif three[i] == '2':
            three[i] = '0'
            val = 0
            for j in range(len_three - 1, -1, -1):
                val += int(three[j]) * (3 ** (len_three - 1 - j))
                three_check.append(val)
            three[i] = '1'
            val = 0
            for j in range(len_three - 1, -1, -1):
                val += int(three[j]) * (3 ** (len_three - 1 - j))
                three_check.append(val)
            three[i] = '2'
        else:
            three[i] = '1'
            val = 0
            for j in range(len_three - 1, -1, -1):
                val += int(three[j]) * (3 ** (len_three - 1 - j))
                three_check.append(val)
            three[i] = '2'
            val = 0
            for j in range(len_three - 1, -1, -1):
                val += int(three[j]) * (3 ** (len_three - 1 - j))
                three_check.append(val)
            three[i] = '0'

    result, max_ = 0, 0
    for i in two_check:
        if i in three_check:
            result = i
            max_ = max(result,max_)
    print(f'#{test_case} {max_}')
