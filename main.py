from randomized_quicksort import quick_sort
from quickSort import quickSort
from hash_table import simulateHashTable
import random
import time
import tracemalloc

# Generate the dataset base on size and the flag.
# size is the size of the array and the values from 1 to size
# Flags are kept to all false by default.
def generate_data(size, random_flag=False, ascending=False, descending=False):
    # Generates Random numbers in the array according to the size
    if random_flag:
        return random.sample(range(1, size + 1), size)
    # Generates ascending numbers in the array according to the size
    if ascending:
        temp = []
        for i in range(size):
            temp.append(i+1)
        return list(temp) # list() is used to decouple the array for a deepcopy
    # Generates descending numbers in the array according to the size
    if descending:
        temp = []
        for i in range(size, 0, -1):
            temp.append(i)
        return list(temp) # list() is used to decouple the array for a deepcopy
    # Generate a list of random array with repeated elements.
    else:
        array_with_repeats = [random.choice(range(1, size+1)) for _ in range(size)]
        return array_with_repeats

def sort_runner(arr, deterministic ,arrayType = 0):
    type = "Randomized quick sort"
    array_data_type = ""

    #flags to determine which data type it is sorting.
    if arrayType == 1:
        array_data_type = "random"
    elif arrayType == 2 :
        array_data_type = "ascending"
    elif arrayType == 3:
        array_data_type = "descending"
    else:
        array_data_type = "random with repeated elements"

    print(array_data_type + " before: ", arr)
    start_time = time.process_time() #start the timer
    if deterministic:
        quickSort(arr)
    else :
        quick_sort(arr)# sort in place
    end_time = time.process_time() #end the timer
    #Print out the proper result
    if deterministic:
        type = "Deterministic quick sort"

    print(type + " time: ", end_time - start_time)

    print(array_data_type + " after sorted: ", arr)
    print('')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    size = 400

    # Generate all the array dataset according to the flag ie. Random, ascending, descending
    arrayRandom = generate_data(size, random_flag=True)
    arrayAscending = generate_data(size, ascending=True)
    arrayDescending = generate_data(size, descending=True)
    array_repeated = generate_data(size)

    # Generate all the array dataset according to the flag ie. Random, ascending, descending
    arrayRandom_2 = generate_data(size, random_flag=True)
    arrayAscending_2 = generate_data(size, ascending=True)
    arrayDescending_2 = generate_data(size, descending=True)
    array_repeated_2 = generate_data(size)

    # Run the Sorter for each type of the array for merge and quick sort
    sort_runner(arrayRandom, False, arrayType=1)
    sort_runner(arrayAscending, False, arrayType=2)
    sort_runner(arrayDescending, False, arrayType=3)
    sort_runner(array_repeated, False)

    sort_runner(arrayRandom_2, True, arrayType=1)
    sort_runner(arrayAscending_2, True, arrayType=2)
    sort_runner(arrayDescending_2, True, arrayType=3)
    sort_runner(array_repeated_2, True)

    #simulate a hashTable run
    simulateHashTable(5)