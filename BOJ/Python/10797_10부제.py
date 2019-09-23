# baekjoon source = "https://www.acmicpc.net/problem/10797"
import sys
N = int(sys.stdin.readline())
car = list(map(int,sys.stdin.readline().split()))
print(car.count(N))