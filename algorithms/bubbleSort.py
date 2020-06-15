from algorithms.utils import swap

def bubbleSort(arr):
    i = 0
    while i < len(arr)-1:
        j = 0
        while j < len(arr)-i-1:
            if arr[j] > arr[j+1]:
                swap(arr, j, j+1)
            j+=1
        i+=1
