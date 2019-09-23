arr = [-1, 3, -9, 6, 7, -6, 1, 5, 3, -2]
n = len(arr)
result = []

for i in range((1 << n)):
    num = []
    for j in range(n):
        if i & (1 << j):
            num.append(arr[j])
    if sum(num) == 0 and num:
        result.append(num)

for i in result:
    print(i)
print()
print(f'총 {len(result)} 개')
