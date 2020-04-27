#!/usr/bin/env python3

class stack:
    def __init__(self, structure=[]):
        self.structure = structure
        self.stackPointer = -1
        self.size = len(structure)

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

    def push(self, o):
        self.stackPointer += 1
        self.structure.append(o)

        self.size += 1
        return self.stackPointer
    
    def pop(self):
        if self.isEmpty():
            print("No more element to pop")
            return
        o = self.top()
        self.stackPointer -= 1
        self.structure.remove(o)

        self.size -= 1
        return o

    def stackInit(self):
        self.structure = []
        self.stackPointer = -1
        self.size = 0


def main():

    S = stack()

    S.push(1)
    print(S)
    S.push(2)
    print(S)
    S.push(3)
    print(S)

    print()
    print(S.isEmpty())
    print(S.top())
    print(S.size)
    print()

    S.stackInit()

    S.push(4)
    print(S)
    S.push(5)
    print(S)
    S.push(6)
    print(S)

    S.pop()
    print(S)
    S.pop()
    print(S)
    S.pop()
    print(S)

    print(S.isEmpty())


if __name__ == "__main__":
    main()
