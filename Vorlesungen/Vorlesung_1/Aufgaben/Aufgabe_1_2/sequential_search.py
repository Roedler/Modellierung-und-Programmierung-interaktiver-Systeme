def sequential_search (haystack, needle):
    i = 0
    while i < len(haystack):
        if haystack[i] == needle:
            return i
        i += 1
    return -1
