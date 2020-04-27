#!/usr/bin/env python3

class node:
    def __init__(self, element, nex = None, pre = None):
        self.element = element
        self.next = nex
        self.prev = pre

    def __str__(self):
        return str(self.element)

class linkedList:
    def __init__(self, arr = []):
        self.head = None
        self.tail = None
        self.length = 0
        if len(arr) > 0:
            for i in arr:
                self.add(i)

    def add(self, e):
        if self.head == None:
            self.head = node(e)
            self.tail = self.head
        else:
            oldTail = self.tail
            self.tail = node(e, pre = oldTail)
            oldTail.next = self.tail

        self.length += 1

    def insert(self, e, i):
        if(self.head != None):
            curr = self.head
        else:
            curr = None

        pos = 0
        while curr != None and pos<i:
            curr = curr.next
            pos += 1

        if curr == self.head:
            oldHead = self.head
            self.head = node(e, nex = oldHead)
            oldHead.prev = self.head

        elif curr == None:
            self.add(e)

        else:
            newNode = node(e, nex = curr, pre = curr.prev)
            curr.prev.next = newNode
            curr.prev = newNode

        self.length += 1


    def remove(self, e):
        if(self.head != None):
            curr = self.head
        else:
            curr = None

        while curr != None:
            if curr.element == e:
                curr.prev.next = curr.next
                curr.next.prev = curr.prev
                del curr
                break

            curr = curr.next

        self.length -= 1

    def removeIndex(self, i):
        if(self.head != None):
            curr = self.head
        else:
            return

        pos = 0
        while curr != None and pos<i:
            curr = curr.next
            pos += 1

        if(curr == self.head):
            self.head = curr.next
            if(self.head != None):
                self.head.prev = None

        elif (curr == self.tail):
            self.tail = curr.prev
            self.tail.next = None

        elif (curr == None):
            return
        else:
            curr.prev.next = curr.next
            curr.next.prev = curr.prev
        
        del curr

        self.length -= 1

    def removeAll(self):
        self.head = None
        self.tail = None
        self.length = 0

    def findIndices(self, e):
        indexList = []
        count = 0

        if(self.head != None):
            curr = self.head
        else:
            curr = None

        while curr != None:
            if curr.element == e:
                indexList.append(count)
            count += 1
            curr = curr.next

        return indexList

    def findIndex(self, e):
        count = 0

        if(self.head != None):
            curr = self.head
        else:
            curr = None

        while curr != None:
            if curr.element == e:
                return count
            count += 1
            curr = curr.next
        
        return None

    def convertToArr(self):
        li = []
        if(self.head != None):
            curr = self.head
        else:
            curr = None

        while curr != None:
            li.append(curr.element)
            curr = curr.next
        return li

    def __str__(self):
        s = ""
        if(self.head != None):
            curr = self.head
        else:
            curr = None

        while curr != None:
            s += str(curr.element) + " "
            curr = curr.next
        return s 


def main():

    li = linkedList([1,2,3,2,5])
    print(li)

    li.insert(6,3)
    print(li)

    li.insert(0,0)
    print(li)

    li.removeIndex(0)
    print(li)

    print(li.length)

    arr = li.convertToArr()
    print(arr)


if __name__ == "__main__":
    main()