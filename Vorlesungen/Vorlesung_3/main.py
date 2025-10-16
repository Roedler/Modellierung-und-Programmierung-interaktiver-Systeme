import random
import time

from Vorlesungen.Vorlesung_2.fakultaet import fakultaet
from Vorlesungen.Vorlesung_3.quicksort import quicksort, quicksortOptimized

def runFakultaet(number):
    print(f"Zahl:\t\t{number:_}")
    startTime = time.perf_counter()
    print(f"Fakultät:\t{fakultaet(number):_}")
    endTime = time.perf_counter()
    print(f"{endTime - startTime} Sekunden")

def runQuicksort(max):
    print("======================== runQuicksort() =========================")

    array = [random.randint(0, max) for _ in range(max)]
    sortedArray = array.copy()
    sortedArray.sort()

    print(f"Unsorted array:\t\t\t\t{array}")

    startTime = time.perf_counter()
    print(f"Quicksort array:\t\t\t{quicksort(array)}")
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden")

    startTime = time.perf_counter()
    print(f"Quicksort sorted array:\t\t{quicksort(sortedArray)}")
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden")
    print("\n")

def runQuicksortOptimized(max):
    print("==================== runQuicksortOptimized() ====================")

    array = [random.randint(0, max) for _ in range(max)]
    sortedArray = array.copy()
    sortedArray.sort()

    print(f"Unsorted array:\t\t\t\t{array}")

    startTime = time.perf_counter()
    quicksortOptimized(array, 0, len(array) - 1)
    print(f"Quicksort array:\t\t\t{array}")
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden")

    startTime = time.perf_counter()
    quicksortOptimized(sortedArray, 0, len(sortedArray) - 1)
    print(f"Quicksort sorted array:\t\t{sortedArray}")
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden")
    print("\n")


# runFakultaet(5)
runQuicksort(10)
runQuicksortOptimized(10)
