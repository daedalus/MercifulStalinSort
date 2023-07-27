from .helpers import merge_arrays

# Merge Sort for array
def merge_sort(arr):
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])
    right_half = merge_sort(arr[mid:])

    return merge_arrays(left_half, right_half)
