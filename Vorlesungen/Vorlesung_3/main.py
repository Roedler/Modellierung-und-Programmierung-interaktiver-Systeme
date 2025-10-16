import random
import time

from Vorlesungen.Vorlesung_2.fakultaet import fakultaet
from Vorlesungen.Vorlesung_3.quicksort import quicksort

# number = 5
# print(f"Zahl:\t\t{number:_}")
# startTime = time.perf_counter()
# print(f"Fakultät:\t{fakultaet(number):_}")
# endTime = time.perf_counter()
# print(f"{endTime - startTime} Sekunden")

maxNumber = 30
array = [random.randint(0, maxNumber) for _ in range(maxNumber)]
print(array)
print(quicksort(array))
