def binary_search_recursive(haystack, left, right, needle):
    if left > right:
        return -1
    mid = left + (right - left) // 2
    if haystack[mid] == needle:
        return mid
    elif haystack[mid] > needle:
        return binary_search_recursive(haystack, left, mid - 1, needle)
    else:
        return binary_search_recursive(haystack, mid + 1, right, needle)
