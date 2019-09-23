# baekjoon source = "https://www.acmicpc.net/problem/14891"

def solution(n, d):
    if d == -1:
        t = wheel[n][0]
        for i in range(7):
            wheel[n][i] = wheel[n][i + 1]
        wheel[n][7] = t
    else:
        t = wheel[n][7]
        for i in range(7, 0, -1):
            wheel[n][i] = wheel[n][i - 1]
        wheel[n][0] = t

wheel = [list(map(int, input())) for _ in range(4)]
k = int(input())

for i in range(k):
    a, b = map(int, input().split())
    if a == 1:
        if wheel[0][2] == wheel[1][6]:
            solution(0, b)
        else:
            if wheel[1][2] == wheel[2][6]:
                solution(0, b)
                solution(1, b * -1)
            else:
                if wheel[2][2] == wheel[3][6]:
                    solution(0, b)
                    solution(1, b * -1)
                    solution(2, b)
                else:
                    solution(0, b)
                    solution(1, b * -1)
                    solution(2, b)
                    solution(3, b * -1)

    elif a == 2:
        if wheel[1][6] != wheel[0][2]:
            solution(0, b * -1)

        if wheel[1][2] == wheel[2][6]:
            solution(1, b)
        else:
            if wheel[2][2] == wheel[3][6]:
                solution(1, b)
                solution(2, b * -1)
            else:
                solution(1, b)
                solution(2, b * -1)
                solution(3, b)

    elif a == 3:
        if wheel[2][2] != wheel[3][6]:
            solution(3, b * -1)

        if wheel[2][6] == wheel[1][2]:
            solution(2, b)
        else:
            if wheel[1][6] == wheel[0][2]:
                solution(2, b)
                solution(1, b * -1)
            else:
                solution(2, b)
                solution(1, b * -1)
                solution(0, b)

    else:
        if wheel[3][6] == wheel[2][2]:
            solution(3, b)
        else:
            if wheel[2][6] == wheel[1][2]:
                solution(3, b)
                solution(2, b * -1)
            else:
                if wheel[1][6] == wheel[0][2]:
                    solution(3, b)
                    solution(2, b * -1)
                    solution(1, b)
                else:
                    solution(3, b)
                    solution(2, b * -1)
                    solution(1, b)
                    solution(0, b * -1)

result = 0
for i in range(4):
    if wheel[i][0]:
        result += 2 ** i
print(result)
