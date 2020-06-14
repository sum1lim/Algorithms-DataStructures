def radixSort(arr):
    main_li = [[] for i in range(10)]
    d = len(str(max(arr)))
    i = 0
    while(i<d):
        while len(arr) > 0:
            s = str(arr[0])
            if(i < len(s)):
                k = int(s[-i-1])
            else:
                k = 0
            main_li[k].append(arr[0])
            del(arr[0])
        for li in main_li:
            while len(li) != 0:
                arr.append(li[0])
                del(li[0])

        i+=1
