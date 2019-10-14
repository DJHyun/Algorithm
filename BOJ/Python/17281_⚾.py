# baekjoon source = "https://www.acmicpc.net/problem/17281"
import itertools
import sys
import time
st = time.time()
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

result = 0
# print(n)
# print(arr)
go = [4, 5, 6, 0, 3, 1, 7, 2, 8]
# itertools.permutations(range(1, 9), 8)
for it in itertools.permutations(range(1, 9), 8):
    it = list(it)
    it.insert(3, 0)
    print(it)
    score = 0
    index = 0
    for count in range(n):
        base = [0, 0, 0]
        out = 0
        while out != 3:

            if arr[count][it[index]] == 0:
                out += 1
            elif arr[count][it[index]] == 1:
                if base[2] == 1:
                    score += 1
                    base[2] = 0
                if base[1] == 1:
                    base[2] = 1
                    base[1] = 0
                if base[0] == 1:
                    base[1] = 1
                base[0] = 1
            elif arr[count][it[index]] == 2:
                if base[2] == 1:
                    score += 1
                    base[2] = 0
                if base[1] == 1:
                    score += 1
                    base[1] = 0
                if base[0] == 1:
                    base[2] = 1
                    base[0] = 0
                base[1] = 1
            elif arr[count][it[index]] == 3:
                if base[2] == 1:
                    score += 1
                    base[2] = 0
                if base[1] == 1:
                    score += 1
                    base[1] = 0
                if base[0] == 1:
                    score += 1
                    base[0] = 0
                base[2] = 1
            elif arr[count][it[index]] == 4:
                for i in range(3):
                    if base[i] == 1:
                        score += 1
                        base[i] = 0
                score += 1

            index += 1
            index %= 9

    result = max(result,score)

print(result)
print(time.time() - st)