def knapsack(s, w):
    B = []

    i = 0
    while i <= len(s):
        tmp = []
        j = 0
        while j <= w:
            tmp.append(0)
            j+=1
        B.append(tmp)
        i+=1

    k = 1
    while k < len(B):
        w = 1
        while w < len(B[k]):
            if(s[k-1][0] > w):
                B[k][w] = B[k-1][w]
            else:
                B[k][w] = max(B[k-1][w], B[k-1][w- s[k-1][0]] + s[k-1][1])

            w += 1
        k += 1

    for row in B:
        print(row)

def main():
    s = [(2,4), (3,7)]
    knapsack(s, 4)




if __name__ == "__main__":
    main()