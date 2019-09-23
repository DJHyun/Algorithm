# baekjoon source = "https://www.acmicpc.net/problem/1107"
'''
5457
3
6 7 8

45
3
4 5 6

45
9
0 1 2 3 4 5 6 7 8

10
1
0
'''

def find(add_num):
    global check_number, final_number, n

    for i in range(10-m):
        tmp_num = add_num + num[i]
        final_number = min(final_number, abs(int(n)-int(tmp_num))+len(tmp_num))
        if tmp_num == n:
            tmp_num += '0000000'
            return
        if len(tmp_num) < 6:
            find(tmp_num)

n = input().strip(' ')
m = int(input())
num = list(map(str, list(range(0, 10))))
if m != 0:
    no = list(input().split())
for i in range(m):
    num.remove(no[i])

st = abs(int(n) - 100)
final_number = float('inf')
find('')
final_number = min(final_number, st)

print(final_number)




#
# for i in range(m):
#     num.remove(no[i])
# print(num)
#
# # 작은것중에 최대
# min_max = -float('inf')
# if length >= 2:
#     for i in range(length - 1, length + 1):
#         if i == length - 1:
#             min_max = int(str(num[9 - m]) * i)
#         else:
#             min_candi = [0] * i
#             idx = 0
#             while idx < i:
#                 if int(n[idx]) in num:
#                     min_candi[idx] = n[idx]
#                 else:
#                     for j in range(9 - m, -1, -1):
#                         if num[j] < int(n[idx]):
#                             min_candi[idx] = str(num[j])
#                             break
#                 idx += 1
#     min_candi = int(''.join(min_candi))
#     print(min_max, min_candi)
#     min_candi = abs(int(n) - min_candi) + len(str(min_candi))
#     min_max = abs(int(n) - min_max) + len(str(min_max))
#     min_max = min(min_max, min_candi)
# else:
#     for i in range(9 - m, -1, -1):
#         if num[i] < int(n):
#             min_max = num[i]
#             break
#     min_max = abs(int(n) - min_max) + 1
#
# print(min_max)
#
# # 큰것 중 최소값
# max_min = float('inf')
# if length >= 2:
#     for i in range(length, length + 2):
#         max_candi = [0] * i
#         idx = 0
#         while idx < i:
#             if int(n[idx]) in num:
#                 max_candi[idx] = n[idx]
#             else:
#                 for j in range(10 - m):
#                     print(j)
#                     if num[j] > int(n[idx]):
#                         max_candi[idx] = str(num[j])
#                         break
#             print('idx', idx)
#             print(max_candi)
#             idx += 1
#         max_candi = int(''.join(max_candi))
#         print(max_candi)
# else:
#     for i in range(10 - m):
#         if num[i] > int(n):
#             max_min = num[i]
#             break
#     max_min = abs(int(n) - max_min) + 1

#
# import itertools
#
# n = input().strip(' ')
# m = int(input())
# num = list(range(0, 10))
# if m != 0:
#     no = list(map(int, input().split()))
# st = abs(int(n) - 100)
# length = len(n)
#
# for i in range(m):
#     num.remove(no[i])
#
# # 최소값 중 최대값
# min_max = -float('inf')
# max_min = float('inf')
# if length >= 2:
#     for i in range(length - 1, length + 1):
#         iter = itertools.product(num, repeat=i)
#         for j in iter:
#             number = ''
#             for z in range(len(j)):
#                 number += str(j[z])
#             if int(number) > int(n):
#                 break
#             min_max = max(min_max, int(number))
#
#     # 최대값 중 최소값
#     for i in range(length, length + 2):
#         iter = itertools.product(num, repeat=i)
#         iter = sorted(iter, reverse=True)
#         for j in iter:
#             number = ''
#             for z in range(len(j)):
#                 number += str(j[z])
#             if int(number) < int(n):
#                 break
#             max_min = min(max_min, int(number))
#
# elif length == 1:
#     for i in range(1, 2):
#         iter = itertools.product(num, repeat=i)
#         for j in iter:
#             number = ''
#             for z in range(len(j)):
#                 number += str(j[z])
#             if int(number) > int(n):
#                 break
#             min_max = max(min_max, int(number))
#
#     for i in range(1, 3):
#         iter = itertools.product(num, repeat=i)
#         iter = sorted(iter, reverse=True)
#         for j in iter:
#             number = ''
#             for z in range(len(j)):
#                 number += str(j[z])
#             if int(number) < int(n):
#                 break
#             max_min = min(max_min, int(number))
#
# # print('---------------')
# # print(min_max, max_min)
# min_max = abs(int(n) - min_max) + len(str(min_max))
# max_min = abs(max_min - int(n)) + len(str(max_min))
# # print(min_max)
# # print(max_min)
# # print(st)
# print(min(max_min, min_max, st))

# result = 0
# max_result = ''
# min_result = ''
# max_flag = True
# min_flag = True
# for i in range(m):
#     num.remove(no[i])
# max_ = -1
# min_ = 10
# for i in range(len(n)):
#     if int(n[i]) in num:
#         max_result += n[i]
#         min_result += n[i]
#         continue
#     else:
#         if max_flag:
#             for a in range(10 - m):
#                 if int(num[a]) < int(n[i]):
#                     max_ = max(max_, int(num[a]))
#                 else:
#                     break
#
#             if max_ != -1:
#                 max_result += str(max_)
#             else:
#                 if len(num) != 0:
#                     max_result = str(num[len(num) - 1]) * (len(n) - 1)
#                     max_flag = False
#
#         if min_flag:
#             for a in range(10 - m - 1, -1, -1):
#                 if int(num[a]) > int(n[i]):
#                     min_ = min(min_, int(num[a]))
#                 else:
#                     break
#
#             if min_ != 10:
#                 min_result += str(min_)
#
#
# if len(num) != 0:
#     if not min_result:
#         if len(num) == 1:
#             if num[0] == 0:
#                 min_result += '100'
#             else:
#                 min_result += str(num[0]) * (len(n) + 1)
#         else:
#             if num[0] == 0:
#                 min_result += str(num[1])
#                 min_result += str(num[0]) * len(n)
#             else:
#                 min_result += str(num[0]) * (len(n) + 1)
#
#     if not max_result:
#         if len(num) == 1:
#             if num[0] == 0:
#                 max_result += '100'
#             else:
#                 max_result += str(num[0]) * len(n)
#         else:
#             max_result += str(num[len(num) - 1]) * (len(n))
# else:
#     max_result = '100'
#     min_result = '100'
#
# print(max_result)
# print(min_result)
# print(st)
# print(min(abs(int(n) - int(max_result)) + len(max_result), abs(int(n) - int(min_result)) + len(min_result), st))
