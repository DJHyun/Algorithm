def quick_sort(arr, l, r):
    if l < r:
        s = partition(arr, l, r)
        quick_sort(arr, l, s - 1)
        quick_sort(arr, s + 1, r)

def partition(arr, p, r):

    i = p - 1

    for j in range(p,r):
        if arr[j] <= arr[r]:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[r] = arr[r], arr[i + 1]

    return i + 1

arr = [1,1,1,1,1,0,0,0,0,0]
quick_sort(arr,0,len(arr)-1)

print(arr)