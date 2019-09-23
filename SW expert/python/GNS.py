import sys

sys.stdin = open("GNS.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    # num = input().split()[1]
    # test_str = input().split()
    # my_dict = {'ZRO':0,'ONE':1,'TWO':2,'THR':3,'FOR':4,'FIV':5,'SIX':6,
    #       'SVN':7,'EGT':8,'NIN':9
    # }
    # my_max = my_dict[test_str[0]]

    # for i in range(0,len(test_str)-1):
    #     my_min = i
    #     for j in range(i+1,len(test_str)):
    #         if my_dict[test_str[my_min]] > my_dict[test_str[j]]:
    #             my_min = j
    #     test_str[my_min], test_str[i] = test_str[i], test_str[my_min]

    # result = ''
    # for i in range(len(test_str)):
    #     if i != len(test_str):
    #         result += test_str[i] + ' '
    #     else:
    #         result += test_str[i]

    # print(f'#{test_case}')
    # print(result)

    num = input().split()[1]
    test_str = input().split()
    result = [[]]*10

    for i in range(len(test_str)):
        if test_str[i][0] == "Z":
            result[0].append(test_str[i])
        elif test_str[i][0] == 'O':
            result[1].append(test_str[i])
        elif test_str[i][0] == 'T':
            if test_str[i][1] == 'W':
                result[2].append(test_str[i])
            else:
                result[3].append(test_str[i])
        elif test_str[i][0] == 'F':
            if test_str[i][1] == 'O':
                result[4].append(test_str[i])
            else:
                result[5].append(test_str[i])
        elif test_str[i][0] == 'S':
            if test_str[i][1] == 'I':
                result[6].append(test_str[i])
            else:
                result[7].append(test_str[i])
        elif test_str[i][0] == 'E':
            result[8].append(test_str[i])
        else:
            result[9].append(test_str[i])
        
    
    print(len(result))

    



    # ///////////////////////////////////////////////////////////////////////////////////
