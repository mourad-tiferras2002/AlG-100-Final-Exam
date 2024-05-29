#!/usr/bin/env python3

""" Q2: Implementing the insertion sort Algo"""

def insertion_sort(arr):
    """insertion_sort - A func that sort an arry using insertion sorting

    Args:
        arr (array of int): The array to sort
    """
    for i in range(1, len(arr)):
        current = arr[i]
        j = i - 1
        while j >= 0 and current < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current


arr = [8, -88, 88, 1988, 2050, 18]
print(f"\n Before sorting array:  {arr}")
insertion_sort(arr)
print(f" \n After Sorteing the  array: {arr} \n")
