import random
import timeit

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)
        merge_sort(right_half)

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[i]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def tim_sort(arr):
    arr.sort()

# A function for measuring the execution time of a sort
def measure_time(sort_func, data):
    start_time = timeit.default_timer()
    sort_func(data)
    return timeit.default_timer() - start_time

# Generate random data for sorting
data_sizes = [10**i for i in range(1, 7)]
for size in data_sizes:
    data = [random.randit(0, 1000) for _ in range(size)]

    # Measure the execution time for each algorithms 
    merge_time = measure_time(merge_sort, data.copy())
    insertion_time = measure_time(insertion_sort, data.copy())
    tim_time = measure_time(tim_sort, data.copy())

    print(f"Data size: {size}")
    print(f"Merge sort time: {merge_time}")
    print(f"Insertion sort time: {insertion_time}")
    print(f"Timsoort time: {tim_time}")
    print()