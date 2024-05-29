#!/usr/bin/env python3

""" Q3: Imlementing the merge sort algorithm"""


def merge_sort(arr):
    """merge_sort - A func that devide the initial array into 2 half's

    Args:
        arr (list of int): array to devide

    Returns:
        A recursive call stack to the merge() func
    """
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge(left_half, right_half)

def merge(left, right):
    """merge - A func that append elements on the right order in both half's

    Args:
        left (list of int): the left half cutted from the initial arr
        right (list of int): the right half cutted from the initial arr

    Returns:
        merged: a sorted list of initial arr
    """
    merged = []
    left_index = right_index = 0

    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            merged.append(left[left_index])
            left_index += 1
        else:
            merged.append(right[right_index])
            right_index += 1

    merged += left[left_index:]
    merged += right[right_index:]

    return merged


arr = [88, 8, 1985, 2050, 18, 17]
print(f"\n Before sorting array:  {arr}")
sorted_arr = merge_sort(arr)
print(f" \n After Sorteing the  array: {sorted_arr} \n")
