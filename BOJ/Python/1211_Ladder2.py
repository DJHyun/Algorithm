# SW Expert Academy
import sys

sys.stdin = open('input (6).txt','r')

for _ in range(10):
    tc = int(input())

    arr = [input().strip().split(" ") for _ in range(100)]

    for i in arr:
        print(i)