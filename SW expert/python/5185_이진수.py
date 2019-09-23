import sys

sys.stdin = open("5185_이진수.txt", "r")

T = int(input())
'''
A	12	1010
B	13	1011
C	14	1100
D	15	1101
E	16	1110
F	17	1111
'''
list_ = {
    '0':'0000','1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000', '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
for test_case in range(1, T + 1):
    n, check = input().split()

    result = ''
    for i in check:
        result += list_[i]
    print(f'#{test_case} {result}')
