# baekjoon source = "https://www.acmicpc.net/problem/2822"

import sys

score = [int(sys.stdin.readline()) for _ in range(8)]
result = []
total = 0
for i in range(5):
    result.append(str(score.index(max(score))+1))
    total += max(score)
    score[score.index(max(score))] = -1
result.sort()
print(total)
print(' '.join(result))