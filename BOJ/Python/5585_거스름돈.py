# baekjoon source = "https://www.acmicpc.net/problem/5585"
import sys

n = int(sys.stdin.readline())
n = 1000 - n
cnt = 0

if n >= 500:
    charge = n // 500
    n -= charge * 500
    cnt += charge

if n >= 100:
    charge = n // 100
    n -= charge * 100
    cnt += charge

if n >= 50:
    charge = n // 50
    n -= charge * 50
    cnt += charge

if n >= 10:
    charge = n // 10
    n -= charge * 10
    cnt += charge

if n >= 5:
    charge = n // 5
    n -= charge * 5
    cnt += charge

if n >= 1:
    charge = n // 1
    n -= charge
    cnt += charge

print(cnt)
