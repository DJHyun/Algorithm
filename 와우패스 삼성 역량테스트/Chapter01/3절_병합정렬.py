'''
16
100 99 98 97 94 95 96 93 92 91 90 89 88 87 86 85
'''

def merge_sort(x):
    if len(x) < 2:
        return x

    left = merge_sort(x[:len(x)//2])
    right = merge_sort(x[len(x)//2:])

    return merge(left,right)

def merge(left,right):
    ne = []
    while left and right:
        if left[0] < right[0]:
            ne.append(left.pop(0))
        else:
            ne.append(right.pop(0))

    if left:
        ne += left
    if right:
        ne += right
    return ne


n = int(input())
numbers = list(map(int,input().split()))
print(numbers)
numbers = merge_sort(numbers)
print(' '.join(map(str,numbers)))