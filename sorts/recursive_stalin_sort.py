import array
from .helpers import merge_arrays

# Merciful Stalin Sort
def recursive_stalin_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    typecode = arr.typecode
    array1 = array.array(typecode)
    array2 = array.array(typecode)

    prev = None

    for elem in arr:
        if prev is None or elem >= prev:
            array1.append(elem)
            prev = elem
        else:
            array2.append(elem)

    # If array2 is empty, the array is already sorted
    if len(array2) == 0:
        return arr[:]

    # Recursively sort array2
    sorted_array2 = recursive_stalin_sort(array2)

    # Merge array1 and sorted_array2
    sorted_arr = merge_arrays(array1, sorted_array2)
    return sorted_arr
