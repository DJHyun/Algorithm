list_ = [1, 2, 1, 3, 2, 4, 3, 5, 3, 6, 4, 7, 5, 8, 5, 9, 6, 10, 6, 11, 7, 12, 11, 13]
node = 13

tree = [[0] * 3 for _ in range(node + 1)]

for i in range(0, len(list_), 2):
    if tree[list_[i]][0] == 0:
        tree[list_[i]][0] = list_[i + 1]
        tree[list_[i + 1]][2] = list_[i]
    else:
        tree[list_[i]][1] = list_[i + 1]
        tree[list_[i + 1]][2] = list_[i]


def preorder(T):
    if T:
        print(T, end=' ')
        preorder(tree[T][0])
        preorder(tree[T][1])


def inorder(T):
    if T:
        preorder(tree[T][0])
        print(T, end=' ')
        preorder(tree[T][1])


def postorder(T):
    if T:
        preorder(tree[T][0])
        preorder(tree[T][1])
        print(T, end=' ')



print('pre', end=' ')
preorder(1)
print()
print('in', end=' ')
inorder(1)
print()
print('post', end=' ')
postorder(1)
print()
