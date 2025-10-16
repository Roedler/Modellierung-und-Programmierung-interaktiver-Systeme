import random
import time

from Vorlesungen.Vorlesung_2.fakultaet import fakultaet
from Vorlesungen.Vorlesung_3.Aufgaben.Aufgabe_3_1.quicksort import quicksort, quicksortOptimized
from testMethod import testMethod


def testFakultaet(number):
    print(f"Zahl:\t\t{number:_}")
    startTime = time.perf_counter()
    print(f"Fakultät:\t{fakultaet(number):_}")
    endTime = time.perf_counter()
    print(f"{endTime - startTime} Sekunden")

def testQuicksort(max):
    print("======================== testQuicksort() =========================")

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

def testQuicksortOptimized(max):
    print("==================== testQuicksortOptimized() ====================")

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


# testFakultaet(5)
testQuicksort(10)
testQuicksortOptimized(10)


# testMethod(fakultaet, 5)
# testMethod(quicksort, [random.randint(0, 10) for _ in range(10)])
