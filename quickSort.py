def quickSort(arr):
    quickSortHelper(arr, 0, len(arr)-1)

def quickSortHelper(arr, low, high):
    if(low < high):
        pivot =  partition(arr, low, high)


        quickSortHelper(arr, low, pivot-1)
        quickSortHelper(arr, pivot+1, high)


def partition(arr, low, high):
    i = low
    j = high-1
    while i<j:
        if arr[i]<arr[high]:
            i+=1
        elif arr[j]>arr[high]:
            j-=1
        else:
            swap(arr, i, j)

    if(arr[j] > arr[high]):
        swap(arr, j, high)
    else:
        j = high
    return j


def swap(arr, a, b):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp

def main():
    arr = [12,234,274,20,1,111,2,34,9,29,199,109,5,203,123,401,568,73,193,122,33,120,40,81,6,221,32]
    quickSort(arr)
    print(arr)


if __name__ == "__main__":
    main()

