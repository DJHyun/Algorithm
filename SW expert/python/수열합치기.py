import sys
sys.stdin = open("수열합치기.txt", "r")

class Node:
    def __init__(self,data,link = None):
        self.data = data
        self.next = link

class Linked_list:
    def __init__(self):
        self.head = None
        self.size = 0

    def insert(self, data):
        if self.size == 0:
            self.head = Node(data)
        else:
            p = self.head
            for _ in range(self.size-1):
                p = p.next
            p.next = Node(data)
        self.size += 1

    def insert_check(self, data):
        p = self.head
        idx = 0

        for _ in range(self.size):
            if p.data > data:
                return idx
            idx +=1
            p = p.next
        
        return idx
    
    def insert_after(self, pre, arr):
        p = self.head
        for _ in range(pre-1):
            p = p.next

        if pre == 0:
            self.head = Node(arr[0],self.head)
            self.size += 1
            p = self.head
            for i in range(1,N):
                p.next = Node(arr[i],p.next)
                p = p.next
                self.size += 1
        else:
            for i in arr:
                p.next = Node(i,p.next)
                p = p.next
                self.size += 1

    def print_list(self):
        p = self.head
        result= []
        for i in range(self.size):
            if i >= self.size - 10:
                result.append(str(p.data))
            p = p.next
        
        return ' '.join(list(reversed(result)))

        
T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int,input().split())
    number = [list(map(int,input().split())) for _ in range(M)]
    test = Linked_list()

    for i in range(M):
        if i == 0:
            for j in number[0]:
                test.insert(j)
        else:
            pre = test.insert_check(number[i][0])
            test.insert_after(pre,number[i])

    print(f'#{test_case} {test.print_list()}')
        
