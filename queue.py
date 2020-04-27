#!/usr/bin/env python3

from linkedList import *

class queue:
    def __init__(self, structure=linkedList()):
        self.structure = structure
        self.size = self.structure.length

    def __str__(self):
        return linkedList.__str__(self.structure)

    def enque(self, e):
        self.structure.add(e)
        self.size += 1

    def deque(self):
        self.structure.removeIndex(0)
        self.size -= 1

    def isEmpty(self):
        if self.structure.head == None:
            return True
        return False

    def front(self):
        return self.structure.head.element

    def queueInit(self):
        self.structure.removeAll()
        self.size = 0


def main():

    Q = queue()

    Q.enque(1)
    print(Q)
    Q.enque(2)
    print(Q)
    Q.enque(3)
    print(Q)

    print()
    print(Q.isEmpty())
    print(Q.front())
    print(Q.size)
    print()

    Q.queueInit()

    Q.enque(4)
    print(Q)
    Q.enque(5)
    print(Q)
    Q.enque(6)
    print(Q)

    Q.deque()
    print(Q)
    Q.deque()
    print(Q)
    Q.deque()
    print(Q)

    print(Q.isEmpty())

if __name__ == "__main__":
    main()