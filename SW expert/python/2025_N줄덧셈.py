import sys
sys.stdin = open('2025_N줄덧셈.txt','r')

result = 0
for i in range(1,int(input())+1):
    result += i

print(result)

