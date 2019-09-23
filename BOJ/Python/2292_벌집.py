# baekjoon source = "https://www.acmicpc.net/problem/2292"
import sys
N = int(sys.stdin.readline().strip())
bee = [2]
i = 1
while bee[-1] <= N:
    bee.append(bee[-1] + 6 * i)
    i += 1

print(i)
print(bee)