def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    smaller = [x for x in array[1:] if x < pivot]
    equal = [x for x in array if x == pivot]
    bigger = [x for x in array[1:] if x > pivot]

    return quicksort(smaller) + equal + quicksort(bigger)

def quicksortOptimized(array, low, high):
    def partition(sub_arr, sub_low, sub_high):
        i = sub_low - 1
        pivot = sub_arr[sub_high]

        for j in range(sub_low, sub_high):
            if sub_arr[j] <= pivot:
                i = i + 1
                sub_arr[i], sub_arr[j] = sub_arr[j], sub_arr[i]

        sub_arr[i + 1], sub_arr[sub_high] = sub_arr[sub_high], sub_arr[i + 1]
        return i + 1

    if low >= high:
        return array

    pi = partition(array, low, high)
    quicksortOptimized(array, low, pi - 1)
    quicksortOptimized(array, pi + 1, high)
