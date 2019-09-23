# baekjoon source = "https://www.acmicpc.net/problem/1158"
import sys

# class Node():
#     def __init__(self, data, link=None):
#         self.data = data
#         self.next = link
#
# class Linked_list():
#     def __init__(self):
#         self.head = Node('Head')
#         self.size = 1
#
#     def L_list(self):
#         p = self.head
#         for i in range(self.size-1):
#             p = p.next
#             print(p.data, end=' ')
#         print()
#
#     def L_insert(self, data):
#         p = self.head
#         for i in range(self.size-1):
#             p = p.next
#         p.next = Node(data)
#         self.size += 1
#
#     def L_pop(self, pre):
#         p = self.head
#         for i in range(pre):
#             p = p.next
#         print(p.data)
#         p.next = p.next.next
#         self.size -= 1

N, M = map(int, sys.stdin.readline().split())
M -= 1
i = 0
# test = Linked_list()
# for i in range(1, N+1):
#     test.L_insert(i)
# test.L_list()
#
# while test.size:
#     i += M
#     test.L_list()
#     if test.size == 1:
#         print(test.L_pop(i % test.size), end='')
#     else:
#         print(test.L_pop(i % test.size), end=', ')
#     if test.size:
#         i %= (test.size + 1)
arr = list(range(1, N + 1))

print('<', end='')
while arr:
    i += M
    if len(arr) == 1:
        print(arr.pop(i % len(arr)), end='')
    else:
        print(arr.pop(i % len(arr)), end=', ')
    if arr:
        i %= (len(arr) + 1)
print('>',end='')
