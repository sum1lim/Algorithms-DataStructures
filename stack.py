#!/usr/bin/env python3

class stack:
    def __init__(self, structure=[]):
        self.structure = structure
        self.stackPointer = -1

    def __str__(self):
        s = ""
        for i in self.structure:
            s += str(i)+ " "
        return s

    def isEmpty(self):
        if(self.stackPointer < 0):
            return True
        return False

    def top(self):
        return self.structure[self.stackPointer]

    def size(self):
        return self.stackPointer + 1

    def push(self, o):
        self.stackPointer += 1
        self.structure.append(o)
        return self.stackPointer
    
    def pop(self):
        if self.isEmpty():
            print("No more element to pop")
            return
        o = self.top()
        self.stackPointer -= 1
        self.structure.remove(o)
        return o

    def stackInit(self):
        self.structure = []