# baekjoon source = "https://www.acmicpc.net/problem/2851"
import sys

score = 0
num = [int(sys.stdin.readline()) for _ in range(10)]
for i in range(10):
    if score + num[i] < 100:
        score += num[i]
    elif score + num[i] == 100:
        score += num[i]
        print(score)
        break
    else:
        if 100 - score < (score + num[i]) - 100:
            print(score)
            break
        else:
            score += num[i]
            print(score)
            break
else:
    print(score)