# baekjoon source = "https://www.acmicpc.net/problem/2749"
import sys

n = int(sys.stdin.readline())
m = 1000000
p = m // 10 * 15
fibo = [0, 1]

for i in range(2, p):
    fibo.append(fibo[i - 1] + fibo[i - 2])
    fibo[i] = fibo[i] % m

print(fibo[n % p])
