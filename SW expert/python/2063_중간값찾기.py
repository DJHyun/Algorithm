import sys
sys.stdin = open("2063_중간값찾기.txt","r")

n = int(input())
numbers = list(map(int,input().split()))
numbers.sort()
print(numbers[n//2])