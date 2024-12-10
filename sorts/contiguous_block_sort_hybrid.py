from collections import deque
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
    n = len(L)
    if n == 0:
        return 0, 0

    start = 0
    best_start, best_end = 0, 0
    min_queue = deque()  # to track the minimum value in the current window
    max_queue = deque()  # to track the maximum value in the current window
    seen = set()  # to track unique elements in the current window

    for end in range(n):
        element = L[end]
        
        # Ensure element is unique in the window
        while element in seen:
            seen.remove(L[start])
            if min_queue[0] == start:
                min_queue.popleft()
            if max_queue[0] == start:
                max_queue.popleft()
            start += 1

        # Add current element to the window
        seen.add(element)

        # Update the min and max queues
        while min_queue and L[min_queue[-1]] >= element:
            min_queue.pop()
        min_queue.append(end)

        while max_queue and L[max_queue[-1]] <= element:
            max_queue.pop()
        max_queue.append(end)

        # Get the current min and max from the queues
        min_val = L[min_queue[0]]
        max_val = L[max_queue[0]]

        # Check if the current window is contiguous
        if max_val - min_val == end - start:
            if end - start > best_end - best_start:
                best_start, best_end = start, end

    return best_start, best_end
    
    
def contiguous_block_sort_hybrid(L):
    """
    Hybrid
    """
    # Base cases
    if (n:= len(L)) <= 1: 
        return L
    if n == 2:
        if L[0] > L[1]: return L[::-1]
        return L
    # Find the longest contiguous subarray
    start, end = longest_contiguous_subarray(L)
    end += 1
    # Split the list into three parts: before, the contiguous subarray, and after
    sub = L[start:end]
    # Create the range for the contiguous subarray
    contiguous_range = list(range(min(sub), max(sub)+1))
    # If the whole array is already contiguous, return it sorted
    if start == 0 and end == n:
        return contiguous_range
    s, e = L[:start], L[end:]
    # Merge the three parts: left, contiguous range, and right
    return merge_sort(merge_arrays(merge_arrays(s, contiguous_range), e))
