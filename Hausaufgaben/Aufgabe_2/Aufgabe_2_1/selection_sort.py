def selection_sort(array, size):
    for index in range(size):
        min_index = index
        for j in range(index + 1, size):
            if array[j] < array[min_index]:
                min_index = j
        (array[index], array[min_index]) = (array[min_index], array[index])
