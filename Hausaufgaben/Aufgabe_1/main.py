import random
import time

from Hausaufgaben.Aufgaben_1.Aufgabe_1_2.sequential_search import sequential_search
from Hausaufgaben.Aufgaben_1.Aufgabe_1_3.binary_search import binary_search

max = 100000000
# array = [2,5,9,10,3,4,7]
array = [random.randint(0,max) for _ in range(max)]
sortedArray = array.copy()
sortedArray.sort()
randomArrayIndex = random.randint(0,max)
randomInt = array[randomArrayIndex]

print("======================== sequential_search() =========================")
startTime = time.perf_counter()
print(f"Position: {sequential_search(array, randomInt)}")
print(array[sequential_search(array, randomInt)])
endTime = time.perf_counter()
print(f"{endTime - startTime} Sekunden")
print("======================================================================")

print("\n========================== binary_search() ===========================")
startTime = time.perf_counter()
print(f"Position: {binary_search(sortedArray, randomInt)}")
print(sortedArray[binary_search(sortedArray, randomInt)])
endTime = time.perf_counter()
print(f"{endTime - startTime} Sekunden")
print("======================================================================")
