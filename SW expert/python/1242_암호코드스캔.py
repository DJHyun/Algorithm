# SW Expert Academy
import sys

sys.stdin = open("1242_암호코드스캔.txt", "r")

def check_len(a):
    global c
    c = 1
    while a:
        check = ['000' * c + '11' * c + '0' * c + '1' * c,
                 '00' * c + '11' * c + '00' * c + '1' * c,
                 '00' * c + '1' * c + '00' * c + '11' * c,
                 '0' * c + '1111' * c + '0' * c + '1' * c,
                 '0' * c + '1' * c + '000' * c + '11' * c,
                 '0' * c + '11' * c + '000' * c + '1' * c,
                 '0' * c + '1' * c + '0' * c + '1111' * c,
                 '0' * c + '111' * c + '0' * c + '11' * c,
                 '0' * c + '11' * c + '0' * c + '111' * c,
                 '000' * c + '1' * c + '0' * c + '11' * c
                 ]
        if a[len(a) - 7 * c:len(a)] in check:
            if (c, a[len(a) - (56 * c):len(a)]) not in final_check:
                final_check.append((c, a[len(a) - (56 * c):len(a)]))
                ch = a[len(a) - (56 * c):len(a)]
                number = []
                for j in range(0, 56 * c, 7 * c):
                    if ch[j:j + 7 * c] in check:
                        number.append(check.index(''.join(ch[j:j + 7 * c])))
                check_number(c, number)
            a = a[:len(a) - (56 * c)].rstrip('0')
            c = 1
        else:
            c += 1

def check_number(c, a):
    global result
    odd, even = 0, 0

    for i in range(7):
        if i % 2:
            even += a[i]
        else:
            odd += a[i]

    if not ((odd * 3 + even + a[7]) % 10):
        result += odd + even + a[7]

T = int(input())
list_ = {
    '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000',
    '9': '1001',
    'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
}
c = 1

for test_case in range(1, T + 1):
    n, m = map(int, input().split())
    check_arr = []
    num = []
    result = 0

    for i in range(n):
        number = list(input())
        if number.count('0') != m:
            if number not in check_arr:
                check_arr.append(number)
                new = ''
                for j in range(m):
                    new += list_[number[j]]
                num.append(list(new.rstrip('0')))

    final_check = []
    for i in range(len(num)):
        check_len(''.join(num[i]))

    print(f'#{test_case} {result}')

# def check_len(a):
#     global c
#     c = 1
#     while a:
#         check = ['000' * c + '11' * c + '0' * c + '1' * c,
#                  '00' * c + '11' * c + '00' * c + '1' * c,
#                  '00' * c + '1' * c + '00' * c + '11' * c,
#                  '0' * c + '1111' * c + '0' * c + '1' * c,
#                  '0' * c + '1' * c + '000' * c + '11' * c,
#                  '0' * c + '11' * c + '000' * c + '1' * c,
#                  '0' * c + '1' * c + '0' * c + '1111' * c,
#                  '0' * c + '111' * c + '0' * c + '11' * c,
#                  '0' * c + '11' * c + '0' * c + '111' * c,
#                  '000' * c + '1' * c + '0' * c + '11' * c
#                  ]
#         if a[len(a) - 7 * c:len(a)] in check:
#             if (c, a[len(a) - (56 * c):len(a)]) not in final_check:
#                 final_check.append((c, a[len(a) - (56 * c):len(a)]))
#             a = a[:len(a) - (56 * c)].rstrip('0')
#             c = 1
#         else:
#             c += 1
#
# T = int(input())
# list_ = {
#     '0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100', '5': '0101', '6': '0110', '7': '0111', '8': '1000',
#     '9': '1001',
#     'A': '1010', 'B': '1011', 'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
# }
# c = 1
#
# for test_case in range(1, T + 1):
#     n, m = map(int, input().split())
#     check_arr = []
#     num = []
#
#     for i in range(n):
#         number = list(input())
#         if number.count('0') != m:
#             if number not in check_arr:
#                 check_arr.append(number[:])
#                 new = ''
#                 for j in range(m):
#                     new += list_[number[j]]
#                 num.append(list(new.rstrip('0')))
#
#     final_check = []
#     for i in range(len(num)):
#         num[i] = check_len(''.join(num[i]))
#
#     number = [[] for _ in range(len(final_check))]
#
#     for i in range(len(final_check)):
#         c = final_check[i][0]
#         check = ['000' * c + '11' * c + '0' * c + '1' * c,
#                  '00' * c + '11' * c + '00' * c + '1' * c,
#                  '00' * c + '1' * c + '00' * c + '11' * c,
#                  '0' * c + '1111' * c + '0' * c + '1' * c,
#                  '0' * c + '1' * c + '000' * c + '11' * c,
#                  '0' * c + '11' * c + '000' * c + '1' * c,
#                  '0' * c + '1' * c + '0' * c + '1111' * c,
#                  '0' * c + '111' * c + '0' * c + '11' * c,
#                  '0' * c + '11' * c + '0' * c + '111' * c,
#                  '000' * c + '1' * c + '0' * c + '11' * c
#                  ]
#         for j in range(0, len(final_check[i][1]), 7 * final_check[i][0]):
#             if final_check[i][1][j:j + 7 * c] in check:
#                 number[i].append(check.index(''.join(final_check[i][1][j:j + 7 * c])))
#
#     result = 0
#     for i in range(len(number)):
#         if number[i] and len(number[i]) == 8:
#             odd, even = 0, 0
#             for j in range(7):
#                 if j % 2:
#                     even += number[i][j]
#                 else:
#                     odd += number[i][j]
#
#             if not ((odd * 3 + even + number[i][7]) % 10):
#                 result += odd + even + number[i][7]
#
#     print(number)
#     print(f'#{test_case} {result}')
