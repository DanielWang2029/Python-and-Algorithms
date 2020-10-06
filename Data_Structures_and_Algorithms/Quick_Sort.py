

from typing import List
import random


# O(n)
def partition(arr: List, left: int, right: int):
    if len(arr) == 0:
        return -1
    if len(arr) == 1:
        return 0
    pivot = arr[right]
    pivotIndex = right
    right = left
    left -= 1
    while right != pivotIndex:
        if arr[right] < pivot:
            left += 1
            temp = arr[right]
            arr[right] = arr[left]
            arr[left] = temp
        right += 1
    temp = arr[left + 1]
    arr[left + 1] = pivot
    arr[pivotIndex] = temp
    return left + 1


def quick_sort(arr: List):
    quick_sort_helper(arr, 0, len(arr) - 1)


# best case O(n * log n) being each sub quick sort has the same num of elms; worst case O(n ^ 2) being already sorted
# average case w/ no replicates is also O(n * log n)
# we could also use random element or the median of three random element as the pivot to avoid worse case scenario
# not stable, meaning the original sequence of duplicated elms might not be preserved
# in-place sorting, meaning little extra memory is used, average case theta(log n), worst case theta(n)
def quick_sort_helper(arr: List, left: int, right: int):
    if left >= right:
        return
    pivot = partition(arr, left, right)
    quick_sort_helper(arr, left, pivot - 1)
    quick_sort_helper(arr, pivot + 1, right)


def partition_three_way(arr: List, left: int, right: int) -> List:
    if len(arr) == 0:
        return [-1, -1]
    pivot = arr[right]
    pivotIndex = right
    left -= 1
    mid = left
    for right in range(left + 1, pivotIndex + 1):
        if arr[right] < pivot:
            left += 1
            mid += 1
            temp = arr[right]
            arr[right] = arr[mid]
            arr[mid] = arr[left]
            arr[left] = temp
        elif arr[right] == pivot:
            mid += 1
            temp = arr[right]
            arr[right] = arr[mid]
            arr[mid] = temp
        right += 1
    return [left + 1, mid]


def quick_sort_three_way(arr: List):
    quick_sort_three_way_helper(arr, 0, len(arr) - 1)


def quick_sort_three_way_helper(arr: List, left: int, right: int):
    if left >= right:
        return
    pivot = partition_three_way(arr, left, right)
    quick_sort_three_way_helper(arr, left, pivot[0] - 1)
    quick_sort_three_way_helper(arr, pivot[1] + 1, right)


input_arr = [100, -7, 9, 35, 64, 83, -35, 0, -83]
quick_sort(input_arr)
print(input_arr)

# there's also a 3-way quicksort which is better when dealing w/ replicates
input_arr = [1, 4, 2, 8, 5, 7, 4, 2, 8, 5, 7, 1, 7, 1, 4, 2, 8, 5]
partition_three_way(input_arr, 0, len(input_arr) - 1)
print(input_arr)
quick_sort_three_way(input_arr)
print(input_arr)
