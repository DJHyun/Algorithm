import sys
sys.stdin = open('6190_정곤이의단조증가하는수.txt','r')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = list(map(int,input().split()))
    max_ = -1

    for i in range(N):
        for j in range(i+1,N):
            result = str(num[i] * num[j])
            for a in range(len(result)-1):
                if int(result[a]) > int(result[a+1]):
                    break
            else:
                if max_ < int(result):
                    max_ = int(result)

    print('#{} {}'.format(test_case, max_))