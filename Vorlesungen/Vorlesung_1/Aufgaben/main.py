import random
import time

from Vorlesungen.Vorlesung_1.Aufgaben.Aufgabe_1_2.sequential_search import sequential_search
from Vorlesungen.Vorlesung_1.Aufgaben.Aufgabe_1_3.binary_search import binary_search

# array = [2,5,9,10,3,4,7]
array = [random.randint(0,100_000_000) for _ in range(100_000_000)]
sortedArray = array.copy()
sortedArray.sort()

print("======================== sequential_search() =========================")
startTime = time.perf_counter()
print(f"Position: {sequential_search(array, 5)}")
print(array[sequential_search(array, 5)])
endTime = time.perf_counter()
print(f"{endTime - startTime} Sekunden")
print("======================================================================")

print("\n========================== binary_search() ===========================")
startTime = time.perf_counter()
print(f"Position: {binary_search(sortedArray, 5)}")
print(sortedArray[binary_search(sortedArray, 5)])
endTime = time.perf_counter()
print(f"{endTime - startTime} Sekunden")
print("======================================================================")
