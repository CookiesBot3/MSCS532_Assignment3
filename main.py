from randomized_quicksort import quick_sort
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

def sort_runner(arr, arrayType = 0):
    type = ""
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
    tracemalloc.start()
    start_time = time.process_time() #start the timer
    quick_sort(arr)# sort in place
    end_time = time.process_time() #end the timer
    first_size, first_peak = tracemalloc.get_traced_memory()
    #Print out the proper result
    print(type + " time: ", end_time - start_time)
    print(type + ": " f"{first_size=}, {first_peak=}")
    tracemalloc.reset_peak()

    print(array_data_type + " after sorted: ", arr)
    # print("Number of operations: ", getMergeN())
    print('\n')

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    size = 500

    # Generate all the array dataset according to the flag ie. Random, ascending, descending
    arrayRandom = generate_data(size, random_flag=True)
    arrayAscending = generate_data(size, ascending=True)
    arrayDescending = generate_data(size, descending=True)
    array_repeated = generate_data(size)

    # Run the Sorter for each type of the array for merge and quick sort
    sort_runner(arrayRandom, arrayType=1)
    sort_runner(arrayAscending, arrayType=2)
    sort_runner(arrayDescending, arrayType=3)
    sort_runner(array_repeated)