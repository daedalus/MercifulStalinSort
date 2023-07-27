import array

# Bubble Sort for array
def bubble_sort(arr):
    n = len(arr)
    sorted_arr = arr[:]

    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if sorted_arr[j] > sorted_arr[j + 1]:
                # Swap
                sorted_arr[j], sorted_arr[j + 1] = sorted_arr[j + 1], sorted_arr[j]

    return sorted_arr
