#!/usr/bin/env python3

import sys


class vertex:
    def __init__(self, element):
        self.element = element


    def __str__(self):
        return str(self.element)


class edge:
    def __init__(self, weight, v1, v2, edgeType = "U", DFStype = "NA"):
        self.weight = weight
        self.org = v1
        self.dest = v2
        if(edgeType == "U" or edgeType == "u"):
            self.edgeType = "undirected"
        elif(edgeType == "D" or edgeType == "d"):
            self.edgeType = "directed"


    def __str__(self):
        return "("+str(self.org)+", "+str(self.dest)+")"



class edgeList:
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
            if e.edgeType == "undirected":
                if e.org == v or e.dest == v:
                    IE.append(e)
            else:
                if e.org == v:
                    IE.append(e)

        return IE

    def degree(self, v):
        deg = 0
        for e in self.edges:
            if e.edgeType == "undirected":
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

    def insertEdge(self, v, w, weight, edgeType="U"):
        self.edges.append(edge(weight, v, w, edgeType))

    def removeVertex(self, v):
        self.vertices.remove(v)

    def removeEdge(self, e):
        self.edges.remove(e)







