import array
from .helpers import merge_arrays #, longest_contiguous_subarray
from .merge_sort import merge_sort
from .quick_sort import quick_sort

"""
Author Darío Clavijo 2024
+---------------+-----------------------------+--------------------------+
| Case          | longest_contiguous_subarray | contiguous_block_sort    |
+---------------+-----------------------------+--------------------------+
| Best Case     | O(n)                        | O(n)                     |
| Average Case  | O(n)                        | O(n log n)               |
| Worst Case    | O(n^2)                      | O(n^2)                   |
+---------------+-----------------------------+--------------------------+
"""


def longest_contiguous_subarray(L):
    # Find the longest contiguous subarray in one pass
    max_len = 0
    max_start = 0
    current_start = 0
    n = len(L)
    
    for i in range(1, len(L)):
        if L[i] != L[i-1] + 1:
            d = i - current_start
            if d > max_len:
                max_len = d
                max_start = current_start
            current_start = i
    
    # Check the last segment
    d = n - current_start
    if d > max_len:
        max_len = d
        max_start = current_start
    
    return max_start, max_len


def contiguous_block_sort_recursive(L):
    """
    Recursive
    """
    # Base cases
    if (n:= len(L)) <= 1: 
        return L
    if n == 2:
        if L[0] > L[1]: return L[::-1]
        return L
    # Find the longest contiguous subarray
    start, max_len = longest_contiguous_subarray(L)
    end = start + max_len
    # Split the list into three parts: before, the contiguous subarray, and after
    sub = L[start:end]
    contiguous_range = list(range(min(sub), max(sub) + 1))
    # If the whole array is already contiguous, return it sorted
    if start == 0 and end == n:
        return contiguous_range
    s = L[:start]
    e = L[end:]
    # Sort the parts that are outside the contiguous subarray (recursively)
    s_sorted = contiguous_block_sort_recursive(s)
    e_sorted = contiguous_block_sort_recursive(e)
    # Create the range for the contiguous subarray and merge everything
    # Merge the three parts: sorted left, contiguous range, and sorted right
    return merge_arrays(merge_arrays(s_sorted, contiguous_range), e_sorted)
