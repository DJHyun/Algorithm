'''
485 241 454 325 452 685 498 890 281 121 486 242 454 325 453 685 499 891 282 122
'''

def quick(x):
    global result
    if len(x) < 2:
        return x

    pivot = x[0]
    for i in range(1, len(x)):
        if x[i] < pivot:
            idx = x.pop(x.index(x[i]))
            x.insert(x.index(pivot), idx)
    print(x, x.index(pivot))

    left = quick(x[:x.index(pivot)])
    print('asdfasdf')
    right = quick(x[x.index(pivot) + 1:])
    print(x, result, left, right)
    return x

result = []
numbers = list(map(int, input().split()))
quick(numbers)
print(numbers)
print(result)
