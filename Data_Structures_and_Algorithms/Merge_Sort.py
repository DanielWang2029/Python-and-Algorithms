

from typing import List


def merge_sort_entire(arr: List[int]):
    merge_sort(arr, 0, len(arr) - 1)


# O(n * log n)
# could also write w/o left and right input, could also use merge() as helper function
# stable, meaning if duplicated value exists, it will preserve their original sequence. e.g. poker cards w/ same number
# not in-place, new arrays are created during the sorting
# space complexity is theta(n)
def merge_sort(arr: List[int], left: int, right: int):
    if left == right:
        return
    # if right - left == 1:
    #     if arr[left] <= arr[right]:
    #         return
    #     else:
    #         temp = arr[left]
    #         arr[left] = arr[right]
    #         arr[right] = temp
    #         return
    mid = (left + right) // 2
    merge_sort(arr, left, mid)
    merge_sort(arr, mid + 1, right)

    # merge
    leftArr, rightArr = arr[left: mid + 1], arr[mid + 1: right + 1]
    i, j, k = 0, 0, left
    while i < len(leftArr) and j < len(rightArr):
        if leftArr[i] < rightArr[j]:
            arr[k] = leftArr[i]
            i += 1
        else:
            arr[k] = rightArr[j]
            j += 1
        k += 1
    while k <= right:
        if i == len(leftArr):
            arr[k] = rightArr[j]
            j += 1
        else:
            arr[k] = leftArr[i]
            i += 1
        k += 1
    del leftArr, rightArr
    return


x = [5, 9, 2, 4, 3, 7, 0, 8, 1, 6]
merge_sort(x, 1, 5)
print(x)
merge_sort_entire(x)
print(x)
