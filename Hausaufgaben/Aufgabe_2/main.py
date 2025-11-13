import random
import time

from Hausaufgaben.Aufgaben_1.Aufgabe_1_3.binary_search import binary_search
from Hausaufgaben.Aufgaben_2.Aufgabe_2_4.binary_search_recursive import binary_search_recursive

max = 10_000_000
# array = [2,5,9,10,3,4,7]
array = [random.randint(0,max) for _ in range(max)]
sortedArray = array.copy()
sortedArray.sort()
randomArrayIndex = random.randint(0,max)
randomInt = array[randomArrayIndex]


# print("========================== bubble_sort() ===========================")
# startTime = time.perf_counter()
#
# bubble_sort(array)
#
# endTime = time.perf_counter()
# print(f"{endTime - startTime} Sekunden")
# print("====================================================================")

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
