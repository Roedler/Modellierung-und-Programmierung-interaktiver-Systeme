def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    smaller = [x for x in array[1:] if x < pivot]
    equal = [x for x in array if x == pivot]
    bigger = [x for x in array[1:] if x > pivot]

    return quicksort(smaller) + equal + quicksort(bigger)

def partition(array, low, high):
    i = low - 1
    pivot = array[high]

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]

    array[i + 1], array[high] = array[high], array[i + 1]
    return i + 1

def quicksortOptimized(array, low, high):
    if low >= high:
        return
    pi = partition(array, low, high)
    quicksortOptimized(array, low, pi - 1)
    quicksortOptimized(array, pi + 1, high)
