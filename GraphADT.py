#!/usr/bin/env python3

import sys

class EdgeList:
    def __init__(self, V=[], E=[]):
        if(type(V) == list):
            self.vertices = V
        else:
            print("​Error: given argument not a list", file=sys.stderr)

        if(type(E) == list):
            self.edges = E
        else:
            print("​Error: given argument not a list", file=sys.stderr)

    def incidentEdges(self, v):
        IE = []
        for e in self.edges:
            if e.type == "undirected":
                if e.org == v or e.dest == v:
                    IE.append(e)
            else:
                if e.org == v:
                    IE.append(e)

        return IE

    def degree(self, v):
        deg = 0
        for e in self.edges:
            if e.type == "undirected":
                if e.org == v or e.dest == v:
                    deg += 1
            else:
                if e.org == v:
                    deg += 1

        return deg

    def areAdjacent(self, v, w):
        for e in self.incidentEdges(v):
            if e.dest == w:
                return True
        return False

    def insertVertex(self, v):
        self.vertices.append(v)

    def insertEdge(self, v, w, weight, type="U"):
        self.edges.append(edge(weight, v, w, type))

    def removeVertex(self, v):
        self.vertices.remove(v)

    def removeEdge(self, e):
        self.edges.remove(e)




class vertex:
    def __init__(self, element):
        self.element = element


    def __str__(self):
        return str(self.element)


class edge:
    def __init__(self, weight, v1, v2, type = "U", DFStype = "NA"):
        self.weight = weight
        self.org = v1
        self.dest = v2
        if(type == "U" or type == "u"):
            self.type = "undirected"
        elif(type == "D" or type == "d"):
            self.type = "directed"


    def __str__(self):
        return "("+str(self.org)+", "+str(self.dest)+")"







