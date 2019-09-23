# baekjoon source = "https://www.acmicpc.net/problem/5543"
import sys
price = [int(sys.stdin.readline()) for _ in range(5)]
print(min(price[:3]) + min(price[3:]) - 50)
