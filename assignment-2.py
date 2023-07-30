"""
Assign 02 - <Matt Mazzaccaro>

Directions:
    * Complete the sorting algorithm functions that are given below. Note that
      it okay (and probably helpful) to define auxiliary/helper functions that
      are called from the functions below.  Refer to the README.md file for
      additional info.

    * NOTE: Remember to add a docstring for each function, and that a reasonable
      coding style is followed (e.g. blank lines between functions).
      Your program will not pass the tests if this is not done!

    * Be sure that you implement your own sorting functions since.
      No credit will be given if Python's built-in sort function is used.
"""

import time
import random
import sys
from math import ceil, log10

sys.setrecursionlimit(10000)


def bubbleSort(a_list):
    """Bubble Sort"""
    start_time = time.time()

    for i in range(len(a_list)):
        for j in range(len(a_list) - 1):
            if a_list[j] > a_list[j + 1]:
                a_list[j], a_list[j + 1] = a_list[j + 1], a_list[j]

    elapsed_time = time.time() - start_time
    return (a_list, elapsed_time)


def mergeSortby3(a_list):
    """Merge Sort by 3"""
    split = len(a_list) // 3

    # Base case: sort sublists of length 1 or 2 using mergeSort
    if len(a_list) <= 2:
        mergeSort(a_list)
        return a_list

    left = a_list[:split]
    right = a_list[(split * 2):]
    middle = a_list[split:(split * 2)]

    mergeSortby3(left)
    mergeSortby3(right)
    mergeSortby3(middle)

    i = 0
    j = 0
    k = 0

    while i < len(left) and j < len(middle) and k < len(right):
        if left[i] < middle[j]:
            if left[i] < right[k]:
                a_list[i + j + k] = left[i]
                i += 1
            else:
                a_list[i + j + k] = right[k]
                k += 1
        else:
            if middle[j] < right[k]:
                a_list[i + j + k] = middle[j]
                j += 1
            else:
                a_list[i + j + k] = right[k]
                k += 1

    while i < len(left) and j < len(middle):
        if left[i] < middle[j]:
            a_list[i + j + k] = left[i]
            i += 1
        else:
            a_list[i + j + k] = middle[j]
            j += 1

    while j < len(middle) and k < len(right):
        if middle[j] < right[k]:
            a_list[i + j + k] = middle[j]
            j += 1
        else:
            a_list[i + j + k] = right[k]
            k += 1

    while i < len(left) and k < len(right):
        if left[i] < right[k]:
            a_list[i + j + k] = left[i]
            i += 1
        else:
            a_list[i + j + k] = right[k]
            k += 1

    while i < len(left):
        a_list[i + j + k] = left[i]
        i += 1

    while j < len(middle):
        a_list[i + j + k] = middle[j]
        j += 1

    while k < len(right):
        a_list[i + j + k] = right[k]
        k += 1

    return a_list


def mergeSort(a_list, split_by_k=2):
    """Merge Sort"""
    start_time = time.time()

    if split_by_k == 3:
        mergeSortby3(a_list)
    else:
        mid = len(a_list) // 2
        left = a_list[:mid]
        right = a_list[mid:]

        if len(a_list) > 1:
            mergeSort(left)
            mergeSort(right)

            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    a_list[k] = left[i]
                    i += 1
                else:
                    a_list[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                a_list[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                a_list[k] = right[j]
                j += 1
                k += 1

    elapsed_time = time.time() - start_time
    return (a_list, elapsed_time)


def partition_low(a_list, low, high):
    """Starting with the first index as the pivot location"""
    pivot = a_list[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1

        while a_list[i] < pivot:
            i += 1

        j -= 1

        while j >= 0 and a_list[j] > pivot:
            j -= 1

        if i >= j:
            return j

        a_list[i], a_list[j] = a_list[j], a_list[i]


def partition_middle(a_list, low, high):
    """Splitting the list based on a middle pivot location"""
    pivot = a_list[(low + high) // 2]
    i = low - 1
    j = high + 1

    while True:
        i += 1

        while a_list[i] < pivot:
            i += 1

        j -= 1

        while j >= 0 and a_list[j] > pivot:
            j -= 1

        if i >= j:
            return j

        a_list[i], a_list[j] = a_list[j], a_list[i]


def quickSort(a_list, pivot='first'):
    """Quick Sort"""
    start_time = time.time()

    if len(a_list) <= 1:
        return a_list

    def _quick_sort(items, low, high):
        """Recursive function for splitting up the list based on the pivot location"""
        if low < high:
            if pivot == 'middle':
                split = partition_middle(items, low, high)
            else:
                split = partition_low(items, low, high)
            _quick_sort(items, low, split)
            _quick_sort(items, split + 1, high)

    _quick_sort(a_list, 0, len(a_list) - 1)

    elapsed_time = time.time() - start_time
    return (a_list, elapsed_time)


def radixSort(a_list):
    """Radix Sort"""
    start_time = time.time()
    max_num_digits = ceil(log10(max(a_list) + 1))

    if max_num_digits == 1:
        return a_list

    for i in range(max_num_digits):
        buckets = [[] for _ in range(10)]

        for num in a_list:
            digit = (num // 10 ** i) % 10
            buckets[digit].append(num)
        a_list = [num for bucket in buckets for num in bucket]

    elapsed_time = time.time() - start_time
    return (a_list, elapsed_time)


def assign02_main():
    """ A 'main' function to be run when our program is run standalone """
    list1 = list(range(5000))
    random.seed(1)
    random.shuffle(list1)

    # run sorting functions
    bubbleRes = bubbleSort(list(list1))
    mergeRes2 = mergeSort(list(list1), split_by_k=2)
    mergeRes3 = mergeSort(list(list1), split_by_k=3)
    quickResA = quickSort(list(list1), pivot='first')
    quickResB = quickSort(list(list1), pivot='middle')
    radixRes = radixSort(list(list1))

    # Print results
    print(f"\nlist1 results (randomly shuffled w/ size = {len(list1)})")
    print(list1[:10])
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])
    print(f"  mergeSort2 time: {mergeRes2[1]:.4f} sec")
    print(mergeRes2[0][:10])
    print(f"  mergeSort3 time: {mergeRes3[1]:.4f} sec")
    print(mergeRes3[0][:10])
    print(f"  quickSortA time: {quickResA[1]:.4f} sec")
    print(quickResA[0][:10])
    print(f"  quickSortB time: {quickResB[1]:.4f} sec")
    print(quickResB[0][:10])
    print(f"  radixSort time: {radixRes[1]:.4f} sec")
    print(radixRes[0][:10])

    # Try with a list sorted in reverse order (worst case for quicksort)
    list2 = list(range(6000, 1000, -1))

    # run sorting functions
    bubbleRes = bubbleSort(list(list2))
    mergeRes2 = mergeSort(list(list2), split_by_k=2)
    mergeRes3 = mergeSort(list(list2), split_by_k=3)
    quickResA = quickSort(list(list2), pivot='first')
    quickResB = quickSort(list(list2), pivot='middle')
    radixRes = radixSort(list(list2))

    # Print results
    print(f"\nlist2 results (sorted in reverse w/ size = {len(list2)})")
    print(list2[:10])
    print(f"  bubbleSort time: {bubbleRes[1]:.4f} sec")
    print(bubbleRes[0][:10])
    print(f"  mergeSort2 time: {mergeRes2[1]:.4f} sec")
    print(mergeRes2[0][:10])
    print(f"  mergeSort3 time: {mergeRes3[1]:.4f} sec")
    print(mergeRes3[0][:10])
    print(f"  quickSortA time: {quickResA[1]:.4f} sec")
    print(quickResA[0][:10])
    print(f"  quickSortB time: {quickResB[1]:.4f} sec")
    print(quickResB[0][:10])
    print(f"  radixSort time: {radixRes[1]:.4f} sec")
    print(radixRes[0][:10])


# Check if the program is being run directly (i.e. not being imported)
if __name__ == '__main__':
    assign02_main()