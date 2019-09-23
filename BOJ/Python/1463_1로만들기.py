# baekjoon source = "https://www.acmicpc.net/problem/1463"

# import sys

# N = int(sys.stdin.readline())
# cnt = 0

# if(N == 1):
#     print(0)
# else:
#     def gogo(N):
#         if N == 1:
#             return N
#         else:
#             if N % 3 == 0:
#                 N = N//3
#             elif N % 2 == 0:
#                 N = N//2
#             else:
#                 N = N -1
#             return gogo(N)
#     print(gogo(N))  

s = 'abcde'
s = s[0].upper()+ s[1:]
print(s)
