# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
"""
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
"""

# 표준 출력 예제
"""
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
"""

import sys

"""
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
"""
sys.stdin = open("재미있는오셀로게임.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, M = list(map(int, input().split()))
    result = []

    for m in range(M):
        test_x, test_y, tz = list(map(int, input().split()))
        tx, ty = test_x - 1, test_y - 1
        result[tx][ty] = tz

    for i in range(n // 2 - 1, n // 2 + 1):
        for j in range(n // 2 - 1, n // 2 + 1):
            if i == j:
                result[i][j] = 2
            else:
                result[i][j] = 1
    for i in result:
        print(i)
    for i in range(m):
        test = list(map(int, input().split()))
        tx, ty, z = test[0] - 1, test[1] - 1, test[2]
        result[tx][ty] = z
        for j in range(2, n):
            for a in range(4):
                x, y = [0, 0, j, -j], [j, -j, 0, 0]
                if tx + x[a] < 0 or tx + x[a] >= n or ty + y[a] < 0 or ty + y[a] >= n:
                    continue
                else:
                    if result[tx + x[a]][ty + y[a]] == z:
                        if x[a] == 0:
                            if y[a] > 0:
                                for aaa in range(ty, ty + y[a]):
                                    if result[tx][aaa] != 0:
                                        result[tx][aaa] = z
                            else:
                                for aaa in range(ty + y[a], ty):
                                    if result[tx][aaa] != 0:
                                        result[tx][aaa] = z
                        else:
                            if x[a] > 0:
                                for aaa in range(tx, tx + x[a]):
                                    if result[aaa][ty] != 0:
                                        result[aaa][ty] = z
                            else:
                                for aaa in range(tx + x[a], tx):
                                    if result[aaa][ty] != 0:
                                        result[aaa][ty] = z
        for j in range(2, n):
            for a in range(4):
                ax, ay = [j, j, -j, -j], [-j, j, -j, j]
                if tx + ax[a] < 0 or tx + ax[a] >= n or ty + ay[a] < 0 or ty + ay[a] >= n:
                    continue
                else:
                    if result[tx + ax[a]][ty + ay[a]] == z:
                        if a == 0:
                            for aaa in zip(range(tx + ax[a], tx, -1), range(ty + ay[a], ty)):
                                if result[aaa[0]][aaa[1]] != 0:
                                    result[aaa[0]][aaa[1]] = z
                        elif a == 1:
                            for aaa in zip(range(tx + ax[a], tx, -1), range(ty + ay[a], ty, -1)):
                                if result[aaa[0]][aaa[1]] != 0:
                                    result[aaa[0]][aaa[1]] = z
                        elif a == 2:
                            for aaa in zip(range(tx + ax[a], tx), range(ty + ay[a], ty)):
                                if result[aaa[0]][aaa[1]] != 0:
                                    result[aaa[0]][aaa[1]] = z
                        elif a == 3:
                            for aaa in zip(range(tx + ax[a], tx), range(ty + ay[a], ty, -1)):
                                if result[aaa[0]][aaa[1]] != 0:
                                    result[aaa[0]][aaa[1]] = z
    cnt1, cnt2 = 0, 0
    for i in result:
        for j in i:
            if j == 1:
                cnt1 += 1
            elif j == 2:
                cnt2 += 1

    print(f'#{test_case} {cnt1} {cnt2}')
