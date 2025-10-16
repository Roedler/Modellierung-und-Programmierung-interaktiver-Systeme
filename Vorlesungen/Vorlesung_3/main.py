import random
import time

from Vorlesungen.Vorlesung_2.fakultaet import fakultaet
from Vorlesungen.Vorlesung_3.quicksort import quicksort

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
    print(f"{endTime - startTime} Sekunden")

    startTime = time.perf_counter()
    print(f"Quicksort sorted array:\t\t{quicksort(sortedArray)}")
    endTime = time.perf_counter()
    print(f"{endTime - startTime} Sekunden")

def testQuicksortOptimized(max):
    print("=================== testQuicksortOptimized() =====================")




# testFakultaet(5)
testQuicksort(10)
testQuicksortOptimized(5)
