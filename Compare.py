import multiprocessing
import os, time, random
from SortFunctions import *

sort_order = {
    0: "Bubble Sort",
    1: 'Selection Sort',
    2: "Insertion Sort",
    3: "Shell Sort",
    4: "Heap Sort",
    5: "Merge Sort",
    6: "Quick Sort",
    7: "Counting Sort",
    8: "Bucket Sort",
    9: "RadixSort"
}

my_list=list(range(25000))
random.shuffle(my_list)


def run_sort(name, arr, lock, nums, length):
    start = 1000 * time.time()
    if name == 0:
        bubble_sort(nums, length)
    elif name == 1:
        selection_sort(nums, length)
    elif name == 2:
        insertion_sort(nums, length)
    elif name == 3:
        shell_sort(nums, length)
    elif name == 4:
        heap_sort(nums, length)
    elif name == 5:
        merge_sort(nums, length)
    elif name == 6:
        quick_sort(nums, 0, length-1)
    elif name == 7:
        counting_sort(nums)
    elif name == 8:
        bucket_sort(nums,30)
    else:
        radixSort(nums)
    end = 1000 * time.time()

    #lock the thread and store the value
    lock.acquire()
    arr[name] = round(end - start, 2)
    lock.release()


def find_winner(sorttime):
    minconstspace = 0
    for i in range(1, 5):
        if sorttime[i] < sorttime[minconstspace]:
            minconstspace = i
    minextraspace = 5
    for i in range(6, 10):
        if sorttime[i] < sorttime[minextraspace]:
            minextraspace = i
    maxindex=0
    for i in range(1, 10):
        if sorttime[i] > sorttime[maxindex]:
            maxindex = i
    # print result
    print("For an array of 25000 random positive integers, the quickest sort is following:")
    print("Winner of sort algorithm takes constant space is:")
    print(sort_order[minconstspace] + " which takes " + str(sorttime[minconstspace]) + " ms")
    print("Winner of sort algorithm takes extra space is:")
    print(sort_order[minextraspace] + " which takes " + str(sorttime[minextraspace]) + " ms")
    print("The slowest algorithm is:")
    print(sort_order[maxindex] + " which takes " + str(sorttime[maxindex]) + " ms")


def main():
    p = multiprocessing.Pool()
    manager = multiprocessing.Manager()
    aim_arr = manager.list([0] * 10)
    lock = manager.Lock()
    n = my_list
    length = 25000
    for i in range(10):
        p.apply_async(run_sort, args=(i, aim_arr, lock, n, length))

    p.close()
    p.join()
    find_winner(aim_arr)


if __name__=='__main__':
    main()