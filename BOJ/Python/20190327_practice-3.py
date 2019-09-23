def preorder(T):
    if T:
        print(T, end=' ')
        preorder(arr[T][0])
        preorder(arr[T][1])

def inorder(T):
    if T:
        inorder(arr[T][0])
        print(T, end=' ')
        inorder(arr[T][1])

def postorder(T):
    if T:
        postorder(arr[T][0])
        postorder(arr[T][1])
        print(T, end=' ')


n = 12
v = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
arr = [[0] * 3 for _ in range(max(v) + 1)]

for i in range(0,max(v)+1,2):
    if not arr[v[i]][0]:
        arr[v[i]][0] = v[i+1]
    else:
        arr[v[i]][1] = v[i+1]
    arr[v[i+1]][2] = v[i]



for i in arr:
    print(i)

preorder(1)
print()
inorder(1)
print()
postorder(1)