

from typing import List


# O(n * 2)
# select the minimum and put it in front of the unsorted part
def selection_sort(arr: List[int]):
    for i in range(0, len(arr) - 1):
        minIndex = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[minIndex]:
                minIndex = j
        temp = arr[minIndex]
        arr[minIndex] = arr[i]
        arr[i] = temp


# 5924370816 -> 0592437816 -> 0159243786 -> 0125943786 -> ...
x = [5, 9, 2, 4, 3, 7, 0, 8, 1, 6]
selection_sort(x)
print(x)


# O(n * 2) for worst and average case, O(n) for best case
# bubble the maximum to the last index
def bubble_sort(arr: List[int]):
    for i in range(len(arr) - 1, 0, -1):
        swap = False
        for j in range(0, i):
            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp
                swap = True
        if not swap:
            break


# 5924370816 -> 5243708169 -> 5243701689 -> 5243016789 -> ...
y = [5, 9, 2, 4, 3, 7, 0, 8, 1, 6]
bubble_sort(y)
print(y)


# O(n * 2) for worst and average case, O(n) for best case
# picking up each elm and putting it in the correct position by pushing all the elms bigger than it rightward
def insertion_sort(arr: List[int]):
    for i in range(1, len(arr)):
        val = arr[i]
        hole = i
        while hole > 0 and arr[hole - 1] > val:
            arr[hole] = arr[hole - 1]
            hole -= 1
        arr[hole] = val


# 5924370816 -> 2594370816 -> 2459370816 -> 2345970816 -> ...
z = [5, 9, 2, 4, 3, 7, 0, 8, 1, 6]
insertion_sort(z)
print(z)
