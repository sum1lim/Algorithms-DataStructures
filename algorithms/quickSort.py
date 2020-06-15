import sys
from algorithms.utils import swap
sys.setrecursionlimit(2147483647)

def linearDeterministicSelection(arr):
    if len(arr) < 5:
        return arr[len(arr)//2]

    median_arr = []
    while(len(arr)):
        group = []
        for _ in range(5):
            if(len(arr)):
                group.append(arr[0])
                del(arr[0])
            else:
                break
        
        i = 0
        while i < 3:
            j = 0
            while j < len(group)-i-1:
                if group[j] > group[j+1]:
                    swap(group, j, j+1)
                j+=1
            i+=1

        median_arr.append(group[len(group)//2])
    
    return linearDeterministicSelection(median_arr)


def partition(arr, low, high, LDS):
    if LDS:
        ideal_pivot = linearDeterministicSelection(arr[low:high+1])
        if(arr[high] == ideal_pivot):
            ideal_pivot_found = True
        else: 
            ideal_pivot_found = False
            value_of_high = arr[high]
            arr[high] = ideal_pivot

    i = low
    j = high-1
    while i<j:
        if LDS and not ideal_pivot_found:
            if (arr[i] == ideal_pivot):
                arr[i] = value_of_high
                ideal_pivot_found = True
            elif (arr[j] == ideal_pivot):
                arr[j] = value_of_high
                ideal_pivot_found = True
    
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

def quickSortHelper(arr, low, high, LDS):
    if(low < high):
        pivot =  partition(arr, low, high, LDS)
        quickSortHelper(arr, low, pivot-1, LDS)
        quickSortHelper(arr, pivot+1, high, LDS)

def quickSort(arr, LDS = False):
    quickSortHelper(arr, 0, len(arr)-1, LDS)
