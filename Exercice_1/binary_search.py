#!/usr/bin/env python3

""" Implementing the Binary search algorithm"""

def binary_search(arr, target):
    """binary_search: is a func that use binary search Algo

    Args:
        arr (int array): array to search in
        target (int): element to find

    Returns:
        False (boolean): if target is not exesting on the array
        middle: the index of the element (target) if exist on the arr
    """
    left = 0
    right = len(arr) - 1

    while left <= right:
        middle = left + (right - left) // 2

        if arr[middle] == target:
            return middle
        elif arr[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return False


arr = [2, 3, 8, 10, 40, 88, 1985, 2017 ,2030]
print(f" \n The arry is {arr}")

try:
    target = int(input("\n Enter an int Value to search -->>  "))
    result = binary_search(arr, target)

    if result != False:
        print(f"--------\n      Element {target} is exist at index {result}")
    else:
        print(f"----------\n    Element {target} is not exists in array\n")
except ValueError or NameError:
    print("Error:  u must enter any integer value")

