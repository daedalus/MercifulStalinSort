import array

# Insertion Sort for array
def insertion_sort(arr):
    sorted_arr = arr[:]

    for i in range(1, len(sorted_arr)):
        key = sorted_arr[i]
        j = i - 1
        # Move elements of sorted_arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j >= 0 and key < sorted_arr[j]:
            sorted_arr[j + 1] = sorted_arr[j]
            j -= 1
        sorted_arr[j + 1] = key

    return sorted_arr
