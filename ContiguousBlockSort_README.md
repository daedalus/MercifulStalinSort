
# Contiguous Block Sort: Hybrid and Recursive Implementations

This repository contains two implementations of the Contiguous Block Sort algorithm: **Hybrid** and **Recursive**. Below is a detailed analysis of their behavior, runtime complexities, and a comparison to other sorting algorithms.

## Contiguous Block Sort

### Hybrid Implementation

The Hybrid implementation of Contiguous Block Sort combines the identification of the longest contiguous subarray with a hybrid sorting approach. It utilizes the Merge Sort algorithm for merging non-contiguous parts.

- **Best Case**: O(n) - The array is fully contiguous and already sorted.
- **Average Case**: O(n log n) - Typical scenario with mixed order.
- **Worst Case**: O(n log n) - Minimal contiguous subarray segments, requiring extensive merging.

### Recursive Implementation

The Recursive implementation takes a divide-and-conquer approach, sorting the non-contiguous segments recursively.

- **Best Case**: O(n) - The array is fully contiguous and already sorted.
- **Average Case**: O(n log n) - Typical scenario with mixed order.
- **Worst Case**: O(n²) - Minimal contiguous subarray segments, requiring extensive recursion and merging.

### Comparison Table

| Case          | Hybrid                | Recursive             |
|---------------|-----------------------|-----------------------|
| Best Case     | O(n)                  | O(n)                  |
| Average Case  | O(n log n)            | O(n log n)            |
| Worst Case    | O(n log n)            | O(n²)                 |

## Algorithm Analysis

### Contiguous Block Sort Behavior

Both implementations rely on identifying the **longest contiguous subarray**, which determines the central "sorted" range of the array. Non-contiguous segments are sorted using either recursive calls or hybrid methods involving Merge Sort.

### Runtime Complexity

- **Best Case**: Occurs when the array is already sorted or entirely contiguous, leading to linear performance.
- **Worst Case**: When the array has minimal contiguous segments, requiring extensive sorting and merging, resulting in quadratic complexity.

### Comparison to Other Algorithms

| Algorithm                         | Best Case    | Average Case | Worst Case   |
|-----------------------------------|--------------|--------------|--------------|
| Bubble Sort                       | O(n)         | O(n²)        | O(n²)        |
| Insertion Sort                    | O(n)         | O(n²)        | O(n²)        |
| Merge Sort                        | O(n log n)   | O(n log n)   | O(n log n)   |
| Quick Sort                        | O(n log n)   | O(n log n)   | O(n²)        |
| Contiguous Block Sort (Hybrid)    | O(n)         | O(n log n)   | O(n log n)   |
| Contiguous Block Sort (Recursive) | O(n)         | O(n log n)   | O(n²)        |
| Merciful Stalin Sort              | O(n)         | O(n log n)   | O(n log n)   |

### Key Observations

- **Bubble Sort** and **Insertion Sort** are simpler algorithms but generally inefficient for large datasets due to their O(n²) worst-case complexity.
- **Merge Sort** provides consistent performance with O(n log n) in all cases, making it a reliable choice for large datasets.
- **Quick Sort** is highly efficient on average but suffers from O(n²) worst-case complexity in unfavorable conditions.
- **Contiguous Block Sort** excels when dealing with datasets containing long contiguous subarrays. The Hybrid implementation leverages Merge Sort for additional efficiency in merging.

### Use Cases

Contiguous Block Sort is particularly effective when the input data exhibits partial ordering or contains long contiguous subarrays. It can outperform traditional algorithms like Quick Sort in such scenarios.

---

## Contributing

Contributions to this repository are welcome. Feel free to open issues or submit pull requests.

