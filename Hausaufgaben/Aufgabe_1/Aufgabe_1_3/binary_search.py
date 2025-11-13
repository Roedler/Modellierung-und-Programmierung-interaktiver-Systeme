def binary_search(haystack, needle):
    low = 0
    high = len(haystack) - 1
    while low <= high:
        mid = (low + high) // 2
        if haystack[mid] == needle:
            return mid
        elif haystack[mid] < needle:
            low = mid + 1
        else:
            high = mid - 1
    return -1
