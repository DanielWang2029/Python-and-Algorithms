

from typing import List


# O(log n)
def binary_search(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_shifted(arr: List[int], target: int) -> int:
    left = 0
    right = len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[left] <= target < arr[mid] or (arr[mid] < arr[left] and (target >= arr[left] or target < arr[mid])):
            right = mid - 1
        else:
            left = mid + 1
    return -1


def binary_search_first_or_last_occurrence(arr: List[int], target: int, first: bool) -> int:
    left = 0
    right = len(arr) - 1
    result = -1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            if first:
                right = mid - 1
            else:
                left = mid + 1
        elif arr[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return result


def count_of_elm_in_sorted_list(arr: List[int], target: int) -> int:
    left = binary_search_first_or_last_occurrence(arr, target, True)
    if left == -1:
        return 0
    right = binary_search_first_or_last_occurrence(arr, target, False)
    return right - left + 1


def number_of_shifts_in_sorted_list(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1
    while arr[left] > arr[right]:
        mid = (left + right) // 2
        if arr[left] == arr[mid]:
            return right
        elif arr[left] < arr[mid]:
            left = mid
        else:
            right = mid
    return left


# another approach for finding the num of shifts, provided in video
def not_my_method(arr: List[int]) -> int:
    left = 0
    right = len(arr) - 1
    while left < right:
        if arr[left] <= arr[right]:
            return left
        mid = (left + right) // 2
        if arr[mid] <= arr[(mid + 1) % len(arr)] and arr[mid] <= arr[mid - 1]:
            return mid
        elif arr[mid] < arr[right]:
            right = mid - 1
        else:
            left = mid + 1
    return -1


input_arr = [-2, 3, 4, 7, 8, 9, 11, 13]
input_target = 11
print(binary_search(input_arr, input_target))  # print 6
print(binary_search(input_arr, 12))  # print -1
print()

# print consecutive numbers (mod 10)
print(binary_search_shifted([-2, 3, 4, 7, 8, 9, 11, 12, 13, 15], -2))
print(binary_search_shifted([3, 4, 7, 8, 9, 11, 12, 13, 15, -2], -2))
print(binary_search_shifted([4, 7, 8, 9, 11, 12, 13, 15, -2, 3], -2))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], -2))
print(binary_search_shifted([8, 9, 11, 12, 13, 15, -2, 3, 4, 7], -2))
print(binary_search_shifted([9, 11, 12, 13, 15, -2, 3, 4, 7, 8], -2))
print(binary_search_shifted([11, 12, 13, 15, -2, 3, 4, 7, 8, 9], -2))
print(binary_search_shifted([12, 13, 15, -2, 3, 4, 7, 8, 9, 11], -2))
print(binary_search_shifted([13, 15, -2, 3, 4, 7, 8, 9, 11, 12], -2))
print(binary_search_shifted([15, -2, 3, 4, 7, 8, 9, 11, 12, 13], -2))
print()

# all print -1
print(binary_search_shifted([-2, 3, 4, 7, 8, 9, 11, 12, 13, 15], -3))
print(binary_search_shifted([-2, 3, 4, 7, 8, 9, 11, 12, 13, 15], 0))
print(binary_search_shifted([-2, 3, 5, 7, 8, 9, 11, 12, 13, 15], 4))
print(binary_search_shifted([-2, 3, 4, 7, 8, 9, 11, 12, 13, 15], 6))
print(binary_search_shifted([-2, 3, 4, 6, 8, 9, 11, 12, 13, 15], 7))
print(binary_search_shifted([-2, 3, 4, 6, 7, 9, 11, 12, 13, 15], 8))
print(binary_search_shifted([-2, 3, 4, 7, 8, 9, 11, 12, 13, 15], 10))
print(binary_search_shifted([-2, 3, 4, 7, 8, 9, 10, 12, 13, 15], 11))
print(binary_search_shifted([-2, 3, 4, 7, 8, 9, 10, 11, 13, 15], 12))
print(binary_search_shifted([-2, 3, 4, 7, 8, 9, 10, 11, 13, 15], 14))
print()

# print consecutive numbers (mod 10)
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], -2))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 3))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 4))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 7))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 8))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 9))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 11))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 12))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 13))
print(binary_search_shifted([7, 8, 9, 11, 12, 13, 15, -2, 3, 4], 15))
print()

# print 3 6 5 1 0
print(binary_search_first_or_last_occurrence([7, 8, 9, 10, 10, 10, 10, 11, 12, 15], 10, True))
print(binary_search_first_or_last_occurrence([7, 8, 9, 10, 10, 10, 10, 11, 12, 15], 10, False))
print(count_of_elm_in_sorted_list([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6], 3))
print(count_of_elm_in_sorted_list([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6], 6))
print(count_of_elm_in_sorted_list([1, 1, 2, 2, 2, 3, 3, 3, 3, 3, 4, 4, 4, 5, 5, 6], 7))
print()

# print 9 - 0
print(number_of_shifts_in_sorted_list([3, 4, 7, 8, 9, 11, 12, 13, 15, -2]))
print(number_of_shifts_in_sorted_list([4, 7, 8, 9, 11, 12, 13, 15, -2, 3]))
print(number_of_shifts_in_sorted_list([7, 8, 9, 11, 12, 13, 15, -2, 3, 4]))
print(number_of_shifts_in_sorted_list([8, 9, 11, 12, 13, 15, -2, 3, 4, 7]))
print(number_of_shifts_in_sorted_list([9, 11, 12, 13, 15, -2, 3, 4, 7, 8]))
print(number_of_shifts_in_sorted_list([11, 12, 13, 15, -2, 3, 4, 7, 8, 9]))
print(number_of_shifts_in_sorted_list([12, 13, 15, -2, 3, 4, 7, 8, 9, 11]))
print(number_of_shifts_in_sorted_list([13, 15, -2, 3, 4, 7, 8, 9, 11, 12]))
print(number_of_shifts_in_sorted_list([15, -2, 3, 4, 7, 8, 9, 11, 12, 13]))
print(number_of_shifts_in_sorted_list([-2, 3, 4, 7, 8, 9, 11, 12, 13, 15]))
