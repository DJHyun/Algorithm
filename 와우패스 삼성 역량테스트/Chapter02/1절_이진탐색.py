'''
30
1 3 7 8 11 12 15 17 20 25 27 38 41 45 48 50 52 55 57 60 64 68 70 72 74 76 78 81 83 97
50

7
1 3 8 11 15 17 20
15
'''

n = int(input())
numbers = list(map(int,input().split()))
find = int(input())
print(n,find)
print(numbers)
left = 0
right = n
mid = (right + left)//2

while left < right:
    print(left,mid,right)
    if numbers[mid] < find:
        left = mid + 1
    elif numbers[mid] > find:
        right = mid -1
    else:
        break

    mid = (right + left)//2

print(mid+1)