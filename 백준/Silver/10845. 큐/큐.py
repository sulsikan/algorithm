import sys

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.chk = None
        self.head = None
        self.tail = None

    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            return

        self.tail.next = new_node
        self.tail = new_node
        return

    def pop(self):
        if self.head is None:
            return print(-1)
        delete_node = self.head
        self.head = self.head.next
        return print(delete_node.data)

    def size(self):
        self.chk = self.head
        cnt = 0
        while self.chk is not None:
            cnt += 1
            self.chk = self.chk.next
        return print(cnt)

    def empty(self):
        if self.head is None:
            return print(1)
        else:
            return print(0)

    def front(self):
        if self.head is None:
            return print(-1)
        return print(self.head.data)

    def back(self):
        if self.head is None:
            return print(-1)
        return print(self.tail.data)


input = sys.stdin.readline

queue = Queue()
n = int(input())

for _ in range(n):
    cmd = input().split()
    if len(cmd) > 1:
        queue.push(cmd[-1])
    else:
        getattr(queue, cmd[0])()
