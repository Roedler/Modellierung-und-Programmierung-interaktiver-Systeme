import time

def testMethod(method, *args):
    print(f"======================== test_{method.__name__}() =========================")

    startTime = time.perf_counter()
    print(*args)
    print(method(*args))
    endTime = time.perf_counter()
    print(f"{(endTime - startTime):.8f} Sekunden\n")
