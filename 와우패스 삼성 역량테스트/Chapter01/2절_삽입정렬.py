'''
35 9 8 18 98 31 58 17 76 45
31
'''

numbers = list(map(int, input().split()))
check = int(input())

result = [numbers[0]]

for i in range(1, len(numbers)):
    for j in range(len(result) - 1, -1, -1):
        if numbers[i] > result[j]:
            result.insert(j + 1, numbers[i])
            break
    else:
        if j == 0:
            result.insert(0, numbers[i])

print(' '.join(map(str,result)))
print(result.index(check)+1)
