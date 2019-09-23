import sys
sys.stdin = open("수열편집.txt", "r")

class Node:
    def __init__(self, data, link = None):
        self.data = data
        self.next = link

class Linked_list:
    def __init__(self):
        self.head = Node('head')
        self.size = 1
    
    def insert(self,data):
        p = self.head
        for _ in range(self.size-1):
            p = p.next
        p.next = Node(data,p.next)
        self.size += 1    

    def print_list(self):
        p = self.head
        for _ in range(self.size-1):
            p = p.next
            print(p.data, end=' ')
        print()

    def I_insert(self,pre,data):
        p = self.head
        for i in range(self.size - 1):
            if i == pre:
                p.next = Node(data,p.next)
                self.size += 1
                break
            p = p.next
    
    def D_delete(self,pre):
        p = self.head
        for i in range(self.size - 1):
            if i == pre:
                p.next = p.next.next
                self.size -= 1
                break
            p = p.next
    
    def C_change(self,pre,data):
        p = self.head
        for i in range(self.size - 1):
            if i == pre:
                p.next.data = data
                break
            p = p.next

    def search(self,index):
        p = self.head.next
        for i in range(self.size - 1):
            if i == index:
                return p.data
            p = p.next
        return -1

T = int(input())
for test_case in range(1, T + 1):
    N, M, L = map(int,input().split())
    num = list(map(int,input().split()))

    test = Linked_list()

    for i in num:
        test.insert(i)


    for i in range(M):
        info = input().split()
    
        if info[0] == 'I':
            test.I_insert(int(info[1]),int(info[2]))
        if info[0] == 'D':
            test.D_delete(int(info[1]))
        if info[0] == 'C':
            test.C_change(int(info[1]),int(info[2]))


    print(f'#{test_case} {test.search(L)}')
