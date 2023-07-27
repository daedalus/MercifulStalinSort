import array

# Quick Sort for array
def quick_sort(arr):
    sorted_arr = arr[:]
    _quick_sort_helper(sorted_arr, 0, len(sorted_arr) - 1)
    return sorted_arr

def _quick_sort_helper(arr, low, high):
    if low < high:
        # Partition the array
        pi = _partition(arr, low, high)
        # Recursively sort elements before and after partition
        _quick_sort_helper(arr, low, pi - 1)
        _quick_sort_helper(arr, pi + 1, high)

def _partition(arr, low, high):
    pivot = arr[high]  # Choosing the last element as pivot
    i = low - 1        # Index of smaller element
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            # Swap arr[i] and arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    # Swap arr[i+1] and arr[high] (or pivot)
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
