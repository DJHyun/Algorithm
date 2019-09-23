import sys
sys.stdin = open("2043_서랍의비밀번호.txt",'r')

p,k = map(int,input().split())

c = 1
while p != k:
    k += 1
    c += 1

print(c)