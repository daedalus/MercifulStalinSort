def fibonacci_shell_sort(arr):
    n = len(arr)
    
    # Generate Fibonacci sequence up to n
    fibs = []
    a, b = 0, 1
    while b <= n:
        fibs.append(b)
        a, b = b, a + b
    
    # Sort using Fibonacci numbers as gaps (in reverse order)
    for gap in reversed(fibs):
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
    return arr

"""
import random
for g in range(1, 31):
  a = [x for x in range(1,g+1)]
  random.shuffle(a)
  b = fibonacci_shell_sort(a)
  print(a == b)
"""
