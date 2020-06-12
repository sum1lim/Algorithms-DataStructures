import numpy as np
from algorithms.quickSort import quickSort
from algorithms.radixSort import radixSort
import time

def is_sorted(li):
    if(all(li[i] <= li[i + 1] for i in range(len(li)-1))): 
        return True
    return False

def main():
    arr = np.random.randint(10000000, size=(100000))
    arr = np.ndarray.tolist(arr)

    test1 = arr[:]
    test2 = arr[:]

    start_time = time.time()
    quickSort(test1)
    elapsed_time = time.time() - start_time
    print("Quick Sort: " + str(elapsed_time) + "sec")
    print("sorted?: " + str(is_sorted(test1)))

    start_time = time.time()
    radixSort(test2)
    elapsed_time = time.time() - start_time
    print("Radixs Sort: " + str(elapsed_time) + "sec")
    print("sorted?: " + str(is_sorted(test2)))


if __name__ == "__main__":
    main()