import random
import time

from Vorlesungen.Vorlesung_1.Aufgaben.Aufgabe_1_3.binary_search import binary_search
from Vorlesungen.Vorlesung_2.Aufgaben.Aufgabe_2_1.bubble_sort import bubble_sort
from Vorlesungen.Vorlesung_2.Aufgaben.Aufgabe_2_4.binary_search_recursive import binary_search_recursive

maxInt = 1_000_000

# array = [2,5,9,10,3,4,7]
array = [random.randint(0,maxInt) for _ in range(maxInt)]
sortedArray = array.copy()
sortedArray.sort()

# print("========================== bubble_sort() ===========================")
# startTime = time.perf_counter()
#
# bubble_sort(array)
#
# endTime = time.perf_counter()
# print(f"{endTime - startTime} Sekunden")
# print("====================================================================")

randomInt = random.randint(0,maxInt)

print("========================== binary_search() ===========================")
startTime = time.perf_counter()
print(f"Position: {binary_search(sortedArray, randomInt)}")
print(sortedArray[binary_search(sortedArray, randomInt)])
endTime = time.perf_counter()
print(f"{endTime - startTime} Sekunden")
print("======================================================================")

print("===================== binary_search_recursive() ======================")
startTime = time.perf_counter()
print(f"Position: {binary_search_recursive(sortedArray, 0, len(sortedArray) - 1, randomInt)}")
print(sortedArray[binary_search_recursive(sortedArray, 0, len(sortedArray) - 1, randomInt)])
endTime = time.perf_counter()
print(f"{endTime - startTime} Sekunden")
print("======================================================================")
