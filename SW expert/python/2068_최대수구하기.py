import sys
sys.stdin = open("2068_최대수구하기.txt","r")

for test_case in range(1, int(input()) + 1):
    print(f'#{test_case} {max(list(map(int,input().split())))}')