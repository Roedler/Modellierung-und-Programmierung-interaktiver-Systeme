def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    smaller = [x for x in array[1:] if x < pivot]
    equal = [x for x in array if x == pivot]
    bigger = [x for x in array[1:] if x > pivot]

    return quicksort(smaller) + equal + quicksort(bigger)
