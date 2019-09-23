import sys
sys.stdin = open("2058_자릿수더하기.txt","r")

result = 0
for num in list(map(int,input())):
    result += num
print(result)