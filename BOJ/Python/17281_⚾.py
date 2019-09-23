# baekjoon source = "https://www.acmicpc.net/problem/17281"

# def check(a, result, out, base):
#     if a == 0:
#         out += 1
#     elif a == 1:
#         for i in range(2, -1, -1):
#             if base[i]:
#                 if i == 2:
#                     result += 1
#                     base[i] = 0
#                 else:
#                     base[i + 1] = 1
#                     base[i] = 0
#         base[0] = 1
#     elif a == 2:
#         for i in range(2, -1, -1):
#             if base[i]:
#                 if i >= 1:
#                     result += 1
#                     base[i] = 0
#                 else:
#                     base[i + 2] = 1
#                     base[i] = 0
#         base[1] = 1
#     elif a == 3:
#         for i in range(2, -1, -1):
#             if base[i]:
#                 result += 1
#                 base[i] = 0
#         base[2] = 1
#     else:
#         result += (base.count(1) + 1)
#         for i in range(3):
#             base[i] = 0
#
#     return [result, out, base]

def solution(b):
    global r, player, cnt

    if b == 9:
        result = 0
        idx = 0
        for i in range(n):
            out = 0
            base = [0, 0, 0]
            while True:
                a = score[i][player[idx]]
                if a == 0:
                    out += 1
                elif a == 1:
                    for i in range(2, -1, -1):
                        if base[i]:
                            if i == 2:
                                result += 1
                                base[i] = 0
                            else:
                                base[i + 1] = 1
                                base[i] = 0
                    base[0] = 1
                elif a == 2:
                    for i in range(2, -1, -1):
                        if base[i]:
                            if i >= 1:
                                result += 1
                                base[i] = 0
                            else:
                                base[i + 2] = 1
                                base[i] = 0
                    base[1] = 1
                elif a == 3:
                    for i in range(2, -1, -1):
                        if base[i]:
                            result += 1
                            base[i] = 0
                    base[2] = 1
                else:
                    result += (base.count(1) + 1)
                    for i in range(3):
                        base[i] = 0

                if out == 3:
                    idx += 1
                    idx %= 9
                    break

                idx += 1
                idx %= 9
        r = max(r, result)
        return
    else:
        if b == 3:
            solution(b + 1)
        else:
            for i in range(1, 9):
                if not visited[i]:
                    visited[i] = 1
                    player[b] = i
                    solution(b + 1)
                    visited[i] = 0

n = int(input())
score = [list(map(int, input().split())) for _ in range(n)]
visited = [0] * 9
player = [0] * 9
r = float('-inf')
solution(0)
print(r)
