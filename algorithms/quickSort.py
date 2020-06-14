import sys
from algorithms.utils import swap
sys.setrecursionlimit(2147483647)

def partition(arr, low, high):
    i = low
    j = high-1
    while i<j:
        if arr[i]<=arr[high]:
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

def quickSortHelper(arr, low, high):
    if(low < high):
        pivot =  partition(arr, low, high)
        quickSortHelper(arr, low, pivot-1)
        quickSortHelper(arr, pivot+1, high)

def quickSort(arr):
    quickSortHelper(arr, 0, len(arr)-1)

