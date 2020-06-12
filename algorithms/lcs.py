def printLCS(path, x, y):
    s = []
    numRows = len(path)
    numCols = len(path[0])

    i = numRows-1
    j = numCols-1

    while i > 0 and j > 0:
        if path[i][j] == "NW":
            s.insert(0, x[j-1])
            i-=1
            j-=1
        elif path[i][j] == "W":
            j -= 1
        else:
            i -= 1

    print(s)

def lcs(x, y):
    llcs = []
    path = []

    n = len(x)
    m = len(y)

    i = 0
    while i <= m:
        tmp = []
        j = 0
        while j <= n:
            tmp.append(0)
            j+=1
        llcs.append(tmp)
        path.append(tmp[:])
        i+=1
    
    i = 1
    while i <= n:
        j = 1
        while j <= m:
            if x[i-1] == y[j-1]:
                llcs[j][i] = llcs[j-1][i-1] + 1
                path[j][i] = "NW"
            elif llcs[j][i-1] >= llcs[j-1][i]:
                llcs[j][i] = llcs[j][i-1]
                path[j][i] = "W"
            else:
                llcs[j][i] = llcs[j-1][i]
                path[j][i] = "N"

            j+=1
        i+=1

    return llcs, path



def main():
    x="chimpanzee"
    y="human"
    llcs,path = lcs(x, y)
    
    for row in llcs:
        print(row)

    print()

    for row in path:
        print(row)

    print()
    printLCS(path, x, y)


if __name__ == "__main__":
    main()
