import random

# Randomized partition function for quicksort
def randomized_partition(arr, low, high):
    # Select a random pivot index between low and high
    pivot_index = random.randint(low, high)
    # Swap the pivot with the last element
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    # Call the regular partition function
    return partition(arr, low, high)

# Partition function to rearrange the array
def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

# Randomized quicksort function
def randomized_quicksort(arr, low = 0, high = None):
    if high is None:
        high = len(arr) - 1

    if low < high:
        # Randomized partition
        pi = randomized_partition(arr, low, high)
        # Recursively sort elements before and after partition
        randomized_quicksort(arr, low, pi - 1)
        randomized_quicksort(arr, pi + 1, high)

# Wrapper function to simplify usage
def quick_sort(arr):
    randomized_quicksort(arr)
    return arr