import array

# Helper to merge two sorted arrays
def merge_arrays(a1, a2):
    typecode = a1.typecode
    result = array.array(typecode)
    i = j = 0

    while i < len(a1) and j < len(a2):
        if a1[i] <= a2[j]:
            result.append(a1[i])
            i += 1
        else:
            result.append(a2[j])
            j += 1

    # Append remaining elements
    result.extend(a1[i:])
    result.extend(a2[j:])

    return result
