# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
import sys

sys.stdin = open("숫자추가.txt", "r")


class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.next = link


class LinkedList:
    def __init__(self):
        self.head = None
        self.size = 0

    def is_empty(self):
        return self.size == 0

    def insert(self, data):
        if self.is_empty():
            self.head = Node(data)
        else:
            p = self.head
            for _ in range(self.size - 1):
                p = p.next
            p.next = Node(data)
        self.size += 1

    def insert_after(self, pre, data):
        p = self.head
        for _ in range(pre - 1):
            p = p.next
        p.next = Node(data, p.next)
        self.size += 1

    def print_list(self, pre):
        p = self.head
        for _ in range(pre):
            p = p.next

        return p.data


T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int, input().split())
    linked = list(map(int, input().split()))

    test = LinkedList()
    for i in linked:
        test.insert(i)

    for _ in range(M):
        index, num = map(int, input().split())
        test.insert_after(index, num)

    print('#{} {}'.format(test_case, test.print_list(L)))
