def radixSort(arr):
    main_li = []
    d = len(str(max(arr)))


    i = 0
    while i < 10:
        main_li.append([])
        i+=1

    i = 0
    while(i<d):
        while len(arr) > 0:
            identifier = float(10**(i+1))
            k = int((((arr[0]/identifier)%1) * 10)//1)
            main_li[k].append(arr[0])
            arr.remove(arr[0])

        for li in main_li:
            while len(li) != 0:
                arr.append(li[0])
                del(li[0])

        i+=1


def main():
    arr = [12,234,274,20,1,111,2,34,9,29,199,109,5,203,123,401,568,73,193,122,33,120,40,81,6,221,32]

    radixSort(arr)
    print(arr)


if __name__ == "__main__":
    main()