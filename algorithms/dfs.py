#!/usr/bin/env python3

from ADT.GraphADT import *
from ADT.StackADT import *
from quickSort import *


class DFSgraph(edgeList):
    def __init__(self, V=[], E=[]):
        edgeList.__init__(self, V, E)

    def DFSinit(self):
        for v in self.vertices:
            v.DFStype = "NA"
            v.DFSpre = 0
            v.DFSpost = 0

        for e in self.edges:
            e.DFStype = "NA"

    def __str__(self):
        s = ""
        for v in self.vertices:
            s += str(v.element) + " "
        return s 

class DFSvertex(vertex):
    def __init__(self, element, DFStype = "NA", DFSorder = 0):
        vertex.__init__(self, element)

        self.DFStype = DFStype
        self.DFSorder = DFSorder

    def __lt__(self, other):
        return (self.DFSorder < other.DFSorder)

    def __gt__(self, other):
        return (self.DFSorder > other.DFSorder)

class DFSedge(edge):
    def __init__(self, weight, v1, v2, type = "U", DFStype = "NA"):
        edge.__init__(self, weight, v1, v2, type)

        self.DFStype = DFStype


    

def DFS(G, v):
    G.DFSinit()
    ordering = 1

    DFShelper(G, v, ordering)

    tmp = G.vertices
    quickSort(tmp)
    s = ""
    for i in tmp:
        s += str(i) + " "
    print(s)

def DFShelper(G, v, ordering):
    v.DFStype = "visited"
    v.DFSorder = ordering
    ordering += 1

    for e in G.incidentEdges(v):
        if e.DFStype == "NA":
            if v == e.org:
                w = e.dest
            else:
                w = e.org
            if w.DFStype == "NA":
                e.DFStype = "Discovery"
                ordering = DFShelper(G,w,ordering)
            else:
                e.DFStype = "Back"

    return ordering


def shortestPath(G, s, t):
    S = stack()
    G.DFSinit()
    found = False

    pathFinder(S, G,s,t, found)

    return S

def pathFinder(S, G,s,t, found):
    s.DFStype = "visited"
    S.push(s)

    if s.element == t.element:
        found = True
        return found

    for e in G.incidentEdges(s):
        if s == e.org:
            w = e.dest
        else:
            w = e.org
        if w.DFStype == "NA":
            e.DFStype == "Discovery"
            found = pathFinder(S, G, w, t, found)
            if found:
                return found
        else:
            e.DFStype == "Back"

    S.pop()


def main():
    A = DFSvertex("A")
    B = DFSvertex("B")
    C = DFSvertex("C")
    D = DFSvertex("D")
    E = DFSvertex("E")
    F = DFSvertex("F")
    G = DFSvertex("G")
    H = DFSvertex("H")
    I = DFSvertex("I")
    J = DFSvertex("J")
    K = DFSvertex("K")
    L = DFSvertex("L")
    M = DFSvertex("M")
    N = DFSvertex("N")
    O = DFSvertex("O")
    P = DFSvertex("P")

    V = [A,B,C,D,E,F,G,H,I,J,K,L,M,N,O,P]

    AB = DFSedge(0, A, B)
    AE = DFSedge(0, A, E)
    AF = DFSedge(0, A, F)
    BC = DFSedge(0, B, C)
    BF = DFSedge(0, B, F)
    CD = DFSedge(0, C, D)
    CG = DFSedge(0, C, G)
    DG = DFSedge(0, D, G)
    DH = DFSedge(0, D, H)
    EF = DFSedge(0, E, F)
    EI = DFSedge(0, E, I)
    FI = DFSedge(0, F, I)
    GK = DFSedge(0, G, K)
    GL = DFSedge(0, G, L)
    HL = DFSedge(0, H, L)
    IJ = DFSedge(0, I, J)
    IM = DFSedge(0, I, M)
    IN = DFSedge(0, I, N)
    KO = DFSedge(0, K, O)
    LP = DFSedge(0, L, P)
    OP = DFSedge(0, O, P)

    E = [AB, AE, AF, BC, BF, CD, CG, DG, DH, EF, EI, FI, GK, GL, HL, IJ, IM, IN, KO, LP, OP]

    G = DFSgraph(V, E)

    p = shortestPath(G, P, A)
    print(p)

    DFS(G, A)


if __name__ == "__main__":
    main()