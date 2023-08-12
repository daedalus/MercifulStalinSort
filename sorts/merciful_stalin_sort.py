import array
from .helpers import merge_arrays

def merciful_stalin_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    typecode = arr.typecode

    # Forward pass: Collect elements in order
    forward_sorted = array.array(typecode)
    forward_remaining = array.array(typecode)

    prev = None
    for elem in arr:
        if prev is None or elem >= prev:
            forward_sorted.append(elem)
            prev = elem
        else:
            forward_remaining.append(elem)

    # Backward pass: Collect elements in reverse order from the remaining elements
    backward_sorted = array.array(typecode)
    backward_remaining = array.array(typecode)

    prev = None
    for elem in reversed(forward_remaining):
        if prev is None or elem <= prev:
            backward_sorted.append(elem)
            prev = elem
        else:
            backward_remaining.append(elem)

    backward_sorted.reverse()

    # Merge sorted from forward and backward passes
    merged_sorted = merge_arrays(forward_sorted, backward_sorted)

    # If no remaining elements, return the merged sorted array
    if len(backward_remaining) == 0:
        return merged_sorted

    # Recursively sort the remaining unsorted elements
    sorted_remaining = merciful_stalin_sort(backward_remaining)

    # Merge all sorted elements and return
    return merge_arrays(merged_sorted, sorted_remaining)
