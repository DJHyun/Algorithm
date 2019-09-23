input = [69, 10, 30, 2, 16, 8, 31, 22]


def merge(arr):

    if len(arr) <= 1:
        return arr

    left = merge(arr[:len(arr)//2])
    right = merge(arr[len(arr)//2:])

    return merge_sort(left,right)

def merge_sort(left, right):
    result = []

    while left and right:
        if left[0] >= right[0]:
            result.append(right.pop(0))
        else:
            result.append(left.pop(0))
    
    if left:
        result.extend(left)
    if right:
        result.extend(right)

    return result

print(merge(input))

list_ = list(range(1000000000))
print(len(list_))
