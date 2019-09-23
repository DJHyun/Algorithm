import sys
sys.stdin = open("암호.txt", "r")

class Node:
    def __init__(self,data, link = None):
        self.data = data
        self.next = link

class Linked_list:
    def __init__(self):
        head = Node('head')
        self.head = head
        self.size = 1
    
    def insert(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            p = self.head
            for i in range(self.size-1):
                p = p.next
            p.next = Node(data)
        self.size += 1
    
    def check(self, M, K):
        p = self.head
        for _ in range(K):
            for i in range(M):
                if p.next == None:
                    p = self.head.next
                else:
                    p = p.next
            if p.next == None:
                p.next =  Node(str(int(p.data) + int(self.head.next.data)),p.next)
            else:
                p.next =  Node(str(int(p.data) + int(p.next.data)),p.next)
            self.size += 1

    def print_list(self):
        p = self.head
        result = [0]*(self.size-1)
        for i in range(self.size-1):
            p = p.next
            result[i] = p.data
        return ' '.join(list(reversed(result))[:10])

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int,input().split())
    num = input().split()
    test = Linked_list()
    
    for i in num:
        test.insert(i)
    
    test.check(M,K)
    print(f'#{test_case} {test.print_list()}')