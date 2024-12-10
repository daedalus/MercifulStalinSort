import array
import random
import time
import os
import matplotlib.pyplot as plt
import sys

# Increase the recursion limit to handle large arrays in recursive algorithms
sys.setrecursionlimit(100000)

# Importing the sorting algorithms from the sorts folder
from sorts.merciful_stalin_sort import merciful_stalin_sort
from sorts.merge_sort import merge_sort
from sorts.quick_sort import quick_sort
from sorts.bubble_sort import bubble_sort
from sorts.insertion_sort import insertion_sort
from sorts.contiguous_block_sort_hybrid import contiguous_block_sort_hybrid
from sorts.contiguous_block_sort_recursive import contiguous_block_sort_recursive

def generate_arrays(size, array_type, shuffle_percent=0):
    """
    Generates an array of a given size and type.

    Parameters:
    - size: int, size of the array.
    - array_type: str, type of the array ('random', 'sorted', 'reverse', 'partial').
    - shuffle_percent: int, percentage of elements to shuffle in partial arrays (X% unsorted).

    Returns:
    - array.array, generated array.
    """
    if array_type == 'random':
        # Fully random array
        random_data = [random.randint(0, size * 10) for _ in range(size)]
    elif array_type == 'sorted':
        # Sorted array
        random_data = list(range(size))
    elif array_type == 'reverse':
        # Reverse sorted array
        random_data = list(range(size, 0, -1))
    elif array_type == 'partial':
        # Partially sorted array (X% unsorted)
        random_data = list(range(size))
        num_to_shuffle = int(size * (shuffle_percent / 100))
        indices = random.sample(range(size), num_to_shuffle)
        values = [random.randint(0, size * 10) for _ in range(num_to_shuffle)]
        for idx, val in zip(indices, values):
            random_data[idx] = val
    else:
        raise ValueError("Invalid array type")

    return array.array('i', random_data)

def benchmark_sorts():
    # List of array sizes to test
    sizes = [100, 500, 1000, 2000, 5000, 10000, 20000]

    # Array types to test
    array_types = [
        ('Random Array', 'random'),
        ('Sorted Array', 'sorted'),
        ('Reverse Sorted Array', 'reverse'),
        ('Partial Sorted (10% Unsorted)', 'partial', 10),
        ('Partial Sorted (30% Unsorted)', 'partial', 30),
        ('Partial Sorted (50% Unsorted)', 'partial', 50)
    ]

    # Create results directory if it doesn't exist
    if not os.path.exists('results'):
        os.makedirs('results')

    print("\n=== Sorting Algorithms Benchmark ===\n")

    # Store results for plotting
    all_results = {}

    for array_type_info in array_types:
        # Unpack array type info
        if array_type_info[1] == 'partial':
            array_type_name, array_type, shuffle_percent = array_type_info
        else:
            array_type_name, array_type = array_type_info
            shuffle_percent = 0

        print(f"--- {array_type_name} ---")
        header = f"{'Array Size':>10} | {'Merciful Stalin (s)':>20} | {'Merge Sort (s)':>15} | {'Quick Sort (s)':>15} | {'Bubble Sort (s)':>15} | {'Insertion Sort (s)':>18} | {'Cb hybrid Sort (s)':>18} | {'Cb recursive Sort (s)':>18} | {'Tim Sort (s)':>18}"
        print(header)
        print("-" * len(header))

        # Initialize dictionaries to store times
        times = {
            'sizes': [],
            'Merciful Stalin Sort': [],
            'Merge Sort': [],
            'Quick Sort': [],
            'Bubble Sort': [],
            'Insertion Sort': [],
            'Contiguous block Sort (Hybrid)': [],
            'Contiguous block Sort (Recursive)': [],
            'Tim Sort': []
        }

        for size in sizes:
            # Generate the array based on the specified type
            original_array = generate_arrays(size, array_type, shuffle_percent)

            # Copies for each sort to keep things fair
            array_for_stalin = original_array[:]
            array_for_merge_sort = original_array[:]
            array_for_quick_sort = original_array[:]
            array_for_bubble = original_array[:]
            array_for_insertion = original_array[:]
            array_for_contiguous_hybrid = original_array[:]
            array_for_contiguous_recursive = original_array[:]
            array_for_tim = original_array[:]

            # Timing Merciful Stalin Sort
            start_time = time.perf_counter()
            sorted_stalin = merciful_stalin_sort(array_for_stalin)
            end_time = time.perf_counter()
            stalin_time = end_time - start_time

            # Timing Merge Sort
            start_time = time.perf_counter()
            sorted_merge_sort = merge_sort(array_for_merge_sort)
            end_time = time.perf_counter()
            merge_sort_time = end_time - start_time

            # Timing Quick Sort
            start_time = time.perf_counter()
            sorted_quick_sort = quick_sort(array_for_quick_sort)
            end_time = time.perf_counter()
            quick_sort_time = end_time - start_time

            # Timing Bubble Sort
            start_time = time.perf_counter()
            sorted_bubble = bubble_sort(array_for_bubble)
            end_time = time.perf_counter()
            bubble_time = end_time - start_time

            # Timing Insertion Sort
            start_time = time.perf_counter()
            sorted_insertion = insertion_sort(array_for_insertion)
            end_time = time.perf_counter()
            insertion_time = end_time - start_time

            # Timing Contiguous block Sort
            start_time = time.perf_counter()
            sorted_contiguous_hybrid = contiguous_block_sort_hybrid(array_for_contiguous_hybrid)
            end_time = time.perf_counter()
            contiguous_hybrid_time = end_time - start_time

            # Timing Contiguous block Sort
            start_time = time.perf_counter()
            sorted_contiguous_recursive = contiguous_block_sort_recursive(array_for_contiguous_recursive)
            end_time = time.perf_counter()
            contiguous_recursive_time = end_time - start_time

            # Timing Tim Sort
            start_time = time.perf_counter()
            sorted_tim = sorted(array_for_tim)
            end_time = time.perf_counter()
            tim_time = end_time - start_time



            # Printing the results
            print(f"{size:>10,} | {stalin_time:>20.6f} | {merge_sort_time:>15.6f} | {quick_sort_time:>15.6f} | {bubble_time:>15.6f} | {insertion_time:>18.6f} | {contiguous_hybrid_time:>18.6f} | {contiguous_recursive_time:>18.6f} | {tim_time:>18.6f}")

            # Store times for plotting
            times['sizes'].append(size)
            times['Merciful Stalin Sort'].append(stalin_time)
            times['Merge Sort'].append(merge_sort_time)
            times['Quick Sort'].append(quick_sort_time)
            times['Bubble Sort'].append(bubble_time)
            times['Insertion Sort'].append(insertion_time)
            times['Contiguous block Sort (Hybrid)'].append(contiguous_hybrid_time)
            times['Contiguous block Sort (Recursive)'].append(contiguous_recursive_time)
            times['Tim Sort'].append(tim_time)

            assert sorted_stalin == sorted_merge_sort

        print("\n")  # Add space between different array type benchmarks

        # Store results for this array type
        all_results[array_type_name] = times

        # Plot and save the graph for this array type
        plot_results(times, array_type_name)

    # Plot special graph for Merciful Stalin Sort performance
    #plot_stalin_performance(all_results)
    plot_single_sort_performance(all_results, "Merciful Stalin Sort")
    plot_single_sort_performance(all_results, "Contiguous block Sort (Hybrid)")
    plot_single_sort_performance(all_results, "Contiguous block Sort (Recursive)")


def plot_results(times, array_type_name):
    sizes = times['sizes']
    plt.figure(figsize=(10, 6))

    plt.plot(sizes, times['Merciful Stalin Sort'], marker='o', label='Merciful Stalin Sort')
    plt.plot(sizes, times['Merge Sort'], marker='s', label='Merge Sort')
    plt.plot(sizes, times['Quick Sort'], marker='^', label='Quick Sort')
    plt.plot(sizes, times['Bubble Sort'], marker='x', label='Bubble Sort')
    plt.plot(sizes, times['Insertion Sort'], marker='d', label='Insertion Sort')
    plt.plot(sizes, times['Contiguous block Sort (Hybrid)'], marker='o', label='Contiguous block Sort (Hybrid)')
    plt.plot(sizes, times['Contiguous block Sort (Recursive)'], marker='p', label='Contiguous block Sort (Recursive)')
    plt.plot(sizes, times['Tim Sort'], marker='*', label='Tim Sort (cpython)')


    plt.title(f'Sorting Algorithms Benchmark - {array_type_name}')
    plt.xlabel('Array Size (log scale)')
    plt.ylabel('Time (seconds) (log scale)')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.xscale('log')
    plt.yscale('log')
    plt.xticks(sizes, labels=[f"{size:,}" for size in sizes], rotation=45)
    plt.tight_layout()

    # Save the plot to the results folder
    sanitized_name = array_type_name.replace(' ', '_').replace('%', '').replace('(', '').replace(')', '').replace('-', '_')
    filename = f"results/{sanitized_name}.png"
    plt.savefig(filename)
    plt.close()

def plot_single_sort_performance(all_results, sort_key):
    # Extract times for Merciful Stalin Sort
    single_sort_times = {}
    for array_type_name, times in all_results.items():
        single_sort_times[array_type_name] = times[sort_key]

    # Assuming all array types have the same sizes
    sizes = all_results[next(iter(all_results))]['sizes']

    plt.figure(figsize=(10, 6))

    for array_type_name in single_sort_times:
        plt.plot(sizes, single_sort_times[array_type_name], marker='o', label=array_type_name)

    plt.title(f'{sort_key} Performance on Different Array Types')
    plt.xlabel('Array Size (log scale)')
    plt.ylabel('Time (seconds) (log scale)')
    plt.legend()
    plt.grid(True, which="both", ls="--", linewidth=0.5)
    plt.xscale('log')
    plt.yscale('log')
    plt.xticks(sizes, labels=[f"{size:,}" for size in sizes], rotation=45)
    plt.tight_layout()

    # Save the plot to the results folder
    filename = f"results/{sort_key.replace(' ','_').replace('(','').replace(')','')}_Performance.png"
    plt.savefig(filename)
    plt.close()

if __name__ == "__main__":
    random.seed(42)
    benchmark_sorts()
