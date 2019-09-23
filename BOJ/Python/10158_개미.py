# baekjoon source = "https://www.acmicpc.net/problem/10158"
'''
6 4
4 1
8

0 1

6 4
4 1
7

0 1


40000 40000
0 0
200000000
'''

w, h = map(int, input().split())
p, q = map(int, input().split())
t = int(input())

p = (t+p) % (w * 2)
q = (t+q) % (h * 2)

if p > w:
    p -= w
    p = w - p
if q > h:
    q -= h
    q = h - q

print(p, q)

# check = w * h
# print(w, h)
# print(p, q)
#
# p_flag, q_flag = 1, 1
# if t % check < check - t % check:
#     for i in range(t % check):
#         if p + 1 > w:
#             p_flag = 0
#         elif p - 1 < 0:
#             p_flag = 1
#
#         if p_flag:
#             p += 1
#         else:
#             p -= 1
#
#         if q + 1 > h:
#             q_flag = 0
#         elif q - 1 < 0:
#             q_flag = 1
#
#         if q_flag:
#             q += 1
#         else:
#             q -= 1
# else:
#     p_flag, q_flag = 0,0
#     for i in range(check - t % check):
#         if p + 1 > w:
#             p_flag = 0
#         elif p - 1 < 0:
#             p_flag = 1
#
#         if p_flag:
#             p += 1
#         else:
#             p -= 1
#
#         if q + 1 > h:
#             q_flag = 0
#         elif q - 1 < 0:
#             q_flag = 1
#
#         if q_flag:
#             q += 1
#         else:
#             q -= 1
#
# print(p, q)
