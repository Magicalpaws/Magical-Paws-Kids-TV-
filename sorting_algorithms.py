"""
Sorting Algorithms Tutorial
Educational implementations of fundamental sorting algorithms
with detailed comments and complexity analysis.
"""

# ============================================================================
# 1. BUBBLE SORT
# ============================================================================
def bubble_sort(arr):
    """
    Bubble Sort: Repeatedly steps through the list, compares adjacent elements,
    and swaps them if they're in the wrong order.
    
    Time Complexity:
    - Best Case: O(n) - when array is already sorted
    - Average Case: O(n²)
    - Worst Case: O(n²) - when array is reverse sorted
    
    Space Complexity: O(1) - only uses a constant amount of extra space
    
    Pros:
    - Very simple to understand and implement
    - Good for educational purposes
    - Requires minimal extra space
    
    Cons:
    - Very inefficient for large datasets
    - Poor performance compared to other algorithms
    
    Example:
    >>> bubble_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Flag to optimize: if no swaps occur, array is sorted
        swapped = False
        
        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # Compare adjacent elements
            if arr[j] > arr[j + 1]:
                # Swap if they're in wrong order
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        
        # If no swaps occurred, array is sorted
        if not swapped:
            break
    
    return arr


# ============================================================================
# 2. SELECTION SORT
# ============================================================================
def selection_sort(arr):
    """
    Selection Sort: Divides array into sorted and unsorted portions.
    Repeatedly finds the minimum element from unsorted portion and moves it to sorted.
    
    Time Complexity:
    - Best Case: O(n²)
    - Average Case: O(n²)
    - Worst Case: O(n²) - always quadratic regardless of input
    
    Space Complexity: O(1) - only uses a constant amount of extra space
    
    Pros:
    - Simple to implement
    - Good for small datasets
    - Minimal memory overhead
    - Useful when memory writes are expensive
    
    Cons:
    - Always O(n²), no best-case improvement
    - Not stable (doesn't preserve relative order of equal elements)
    - Inefficient for large datasets
    
    Example:
    >>> selection_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    
    # Traverse through all array elements
    for i in range(n):
        # Find the minimum element in remaining unsorted array
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        # Swap the found minimum element with the first element
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr


# ============================================================================
# 3. INSERTION SORT
# ============================================================================
def insertion_sort(arr):
    """
    Insertion Sort: Builds the sorted array one item at a time.
    Iterates through an input array, and for each element, finds the place
    it belongs in the sorted portion and inserts it there.
    
    Time Complexity:
    - Best Case: O(n) - when array is already sorted
    - Average Case: O(n²)
    - Worst Case: O(n²) - when array is reverse sorted
    
    Space Complexity: O(1) - only uses a constant amount of extra space
    
    Pros:
    - Very efficient for small datasets
    - Adaptive: O(n) when data is nearly sorted
    - Stable sort: maintains relative order of equal elements
    - Online: can sort data as it receives it
    - Works well with linked lists (unlike bubble sort)
    
    Cons:
    - O(n²) for large datasets
    - Not as efficient as merge sort or quick sort
    
    Example:
    >>> insertion_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):
        key = arr[i]  # Element to be inserted
        j = i - 1     # Index of the last element in sorted portion
        
        # Move elements of arr[0..i-1] that are greater than key one position ahead
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        # Insert the key at its correct position
        arr[j + 1] = key
    
    return arr


# ============================================================================
# 4. MERGE SORT
# ============================================================================
def merge_sort(arr):
    """
    Merge Sort: Divide-and-conquer algorithm.
    Divides array in half, recursively sorts each half, then merges them back.
    
    Time Complexity:
    - Best Case: O(n log n)
    - Average Case: O(n log n)
    - Worst Case: O(n log n) - guaranteed O(n log n) performance
    
    Space Complexity: O(n) - requires extra space for merging
    
    Pros:
    - Guaranteed O(n log n) time complexity
    - Stable sort: maintains relative order of equal elements
    - Predictable performance
    - Good for large datasets
    - Works well with linked lists
    
    Cons:
    - Requires O(n) extra space
    - Slower than quicksort on average for random data
    - Not in-place
    
    Example:
    >>> merge_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr
    
    # Divide: find the middle point
    mid = len(arr) // 2
    
    # Divide: split array into two halves
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    
    # Conquer: merge the sorted halves
    return merge(left, right)


def merge(left, right):
    """
    Helper function for merge sort.
    Merges two sorted arrays into one sorted array.
    
    Time Complexity: O(n + m) where n and m are lengths of left and right
    Space Complexity: O(n + m) - new array for merged result
    """
    result = []
    i = j = 0
    
    # Compare elements from left and right arrays
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    # Add remaining elements from left array
    result.extend(left[i:])
    
    # Add remaining elements from right array
    result.extend(right[j:])
    
    return result


# ============================================================================
# 5. QUICK SORT
# ============================================================================
def quick_sort(arr):
    """
    Quick Sort: Divide-and-conquer algorithm.
    Picks a pivot element, partitions array around it, recursively sorts partitions.
    
    Time Complexity:
    - Best Case: O(n log n) - when pivot divides array evenly
    - Average Case: O(n log n) - typically good performance
    - Worst Case: O(n²) - when pivot is always smallest/largest (rare with good pivot selection)
    
    Space Complexity: O(log n) - recursive call stack (in-place partitioning)
    
    Pros:
    - Fast average-case performance O(n log n)
    - In-place sorting: uses O(log n) extra space
    - Cache-friendly: accesses elements sequentially
    - Practical: often faster than merge sort in practice
    - Works well for random data
    
    Cons:
    - Worst case O(n²) (rare but possible)
    - Not stable: may not preserve relative order of equal elements
    - Performance depends on pivot selection
    - Not adaptive: same performance on sorted data as random data
    
    Example:
    >>> quick_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    if len(arr) <= 1:
        return arr
    
    # Choose pivot (using middle element for better average performance)
    pivot = arr[len(arr) // 2]
    
    # Partition array into three parts
    left = [x for x in arr if x < pivot]      # Elements less than pivot
    middle = [x for x in arr if x == pivot]   # Elements equal to pivot
    right = [x for x in arr if x > pivot]     # Elements greater than pivot
    
    # Recursively sort left and right, then combine
    return quick_sort(left) + middle + quick_sort(right)


def quick_sort_inplace(arr, low=0, high=None):
    """
    In-place Quick Sort variant using partitioning.
    This version sorts the array in-place with O(log n) space complexity.
    
    Time Complexity: Same as quick_sort
    Space Complexity: O(log n) - only recursive call stack
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # Partition and get pivot index
        pivot_idx = partition(arr, low, high)
        
        # Recursively sort left partition
        quick_sort_inplace(arr, low, pivot_idx - 1)
        
        # Recursively sort right partition
        quick_sort_inplace(arr, pivot_idx + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    Helper function for in-place quick sort.
    Partitions array around a pivot and returns the pivot index.
    """
    pivot = arr[high]
    i = low - 1
    
    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


# ============================================================================
# 6. HEAP SORT (Bonus)
# ============================================================================
def heap_sort(arr):
    """
    Heap Sort: Uses a heap data structure to sort.
    
    Time Complexity:
    - All cases: O(n log n) - guaranteed
    
    Space Complexity: O(1) - in-place (excluding recursive call stack)
    
    Pros:
    - Guaranteed O(n log n) performance
    - In-place sorting
    - Good worst-case performance
    
    Cons:
    - Not stable
    - Not adaptive: same performance on sorted data
    - Worse cache locality than quicksort
    
    Example:
    >>> heap_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    n = len(arr)
    
    # Build max heap
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    
    # Extract elements from heap one by one
    for i in range(n - 1, 0, -1):
        # Move current root (max) to end
        arr[0], arr[i] = arr[i], arr[0]
        
        # Heapify reduced heap
        heapify(arr, i, 0)
    
    return arr


def heapify(arr, n, i):
    """
    Helper function for heap sort.
    Maintains heap property for subtree rooted at index i.
    """
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[largest]:
        largest = left
    
    if right < n and arr[right] > arr[largest]:
        largest = right
    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)


# ============================================================================
# 7. COUNTING SORT (Bonus - for non-negative integers)
# ============================================================================
def counting_sort(arr, max_val=None):
    """
    Counting Sort: Non-comparative sort for non-negative integers.
    
    Time Complexity: O(n + k) where k is the range of input
    Space Complexity: O(k) where k is the range of input
    
    Pros:
    - Linear time complexity O(n + k)
    - Stable sort
    - Very fast for small range of integers
    
    Cons:
    - Only works with non-negative integers (or can be modified for negatives)
    - Extra space proportional to range
    - Not comparison-based
    
    Example:
    >>> counting_sort([64, 34, 25, 12, 22, 11, 90])
    [11, 12, 22, 25, 34, 64, 90]
    """
    if not arr:
        return arr
    
    # Find maximum value if not provided
    if max_val is None:
        max_val = max(arr)
    
    # Create count array
    count = [0] * (max_val + 1)
    
    # Count occurrences of each element
    for num in arr:
        count[num] += 1
    
    # Reconstruct sorted array
    result = []
    for i in range(len(count)):
        result.extend([i] * count[i])
    
    return result


# ============================================================================
# UTILITY FUNCTIONS
# ============================================================================
def compare_algorithms(arr):
    """
    Compare all sorting algorithms on the same input.
    Returns dictionary with algorithm names and sorted results.
    """
    import copy
    
    results = {
        'Original': arr.copy(),
        'Bubble Sort': bubble_sort(copy.copy(arr)),
        'Selection Sort': selection_sort(copy.copy(arr)),
        'Insertion Sort': insertion_sort(copy.copy(arr)),
        'Merge Sort': merge_sort(copy.copy(arr)),
        'Quick Sort': quick_sort(copy.copy(arr)),
        'Heap Sort': heap_sort(copy.copy(arr)),
    }
    
    return results


def print_comparison(arr):
    """
    Print comparison of all sorting algorithms with timing.
    """
    import time
    
    results = {}
    
    algorithms = [
        ('Bubble Sort', bubble_sort),
        ('Selection Sort', selection_sort),
        ('Insertion Sort', insertion_sort),
        ('Merge Sort', merge_sort),
        ('Quick Sort', quick_sort),
        ('Heap Sort', heap_sort),
    ]
    
    print(f"Sorting array of {len(arr)} elements: {arr[:10]}..." if len(arr) > 10 else f"Sorting array: {arr}")
    print("-" * 60)
    
    for name, func in algorithms:
        test_arr = arr.copy()
        start = time.time()
        sorted_arr = func(test_arr)
        end = time.time()
        
        elapsed = (end - start) * 1000  # Convert to milliseconds
        print(f"{name:20} | Time: {elapsed:10.4f} ms | Result: {sorted_arr[:10]}..." if len(sorted_arr) > 10 else f"{name:20} | Time: {elapsed:10.4f} ms | Result: {sorted_arr}")


# ============================================================================
# TEST AND EXAMPLES
# ============================================================================
if __name__ == "__main__":
    # Test data
    test_array = [64, 34, 25, 12, 22, 11, 90, 33, 55, 44]
    
    print("=" * 60)
    print("SORTING ALGORITHMS TUTORIAL")
    print("=" * 60)
    print(f"\nOriginal Array: {test_array}\n")
    
    # Test each algorithm
    print("BUBBLE SORT:")
    print(f"Result: {bubble_sort(test_array.copy())}\n")
    
    print("SELECTION SORT:")
    print(f"Result: {selection_sort(test_array.copy())}\n")
    
    print("INSERTION SORT:")
    print(f"Result: {insertion_sort(test_array.copy())}\n")
    
    print("MERGE SORT:")
    print(f"Result: {merge_sort(test_array.copy())}\n")
    
    print("QUICK SORT:")
    print(f"Result: {quick_sort(test_array.copy())}\n")
    
    print("HEAP SORT:")
    print(f"Result: {heap_sort(test_array.copy())}\n")
    
    print("=" * 60)
    print("\nCOMPARISON OF ALL ALGORITHMS:")
    print_comparison(test_array)
    
    # Test with larger array
    import random
    large_array = [random.randint(1, 100) for _ in range(100)]
    print("\n" + "=" * 60)
    print("PERFORMANCE ON LARGER ARRAY (100 elements):")
    print_comparison(large_array)
