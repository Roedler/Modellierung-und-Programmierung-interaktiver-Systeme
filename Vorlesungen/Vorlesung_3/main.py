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
    print("======================== testQuicksort() =========================")

    array = [random.randint(0, max) for _ in range(max)]
    sortedArray = array.copy()
    sortedArray.sort()

    print(f"Unsorted array:\t\t\t\t{array}")

    startTime = time.perf_counter()
    print(f"Quicksort array:\t\t\t{quicksort(array)}")
    endTime = time.perf_counter()
    print(f"{endTime - startTime} Sekunden")

    startTime = time.perf_counter()
    print(f"Quicksort sorted array:\t\t{quicksort(sortedArray)}")
    endTime = time.perf_counter()
    print(f"{endTime - startTime} Sekunden")
    print("\n")

def runQuicksortOptimized(max):
    print("==================== testQuicksortOptimized() ====================")
    array = [random.randint(0, max) for _ in range(max)]
    sortedArray = array.copy()
    sortedArray.sort()

    print(f"Unsorted array:\t\t\t\t{array}")

    startTime = time.perf_counter()
    print(f"Quicksort array:\t\t\t{quicksortOptimized(array, 0, len(array) - 1)}")
    endTime = time.perf_counter()
    print(f"{endTime - startTime} Sekunden")

    startTime = time.perf_counter()
    print(f"Quicksort sorted array:\t\t{quicksortOptimized(sortedArray, 0, len(sortedArray) - 1)}")
    endTime = time.perf_counter()
    print(f"{endTime - startTime} Sekunden")
    print("\n")


# runFakultaet(5)
runQuicksort(10)
runQuicksortOptimized(10)
