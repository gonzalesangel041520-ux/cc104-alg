import time

arr = list(range(1_000_000))

# O(1) access - instant, no matter the size
start = time.perf_counter()  # use perf_counter() not time()
x = arr[500_000]
end = time.perf_counter()
print("O(1) access time:", end - start)

# O(n) search - scans 999,999 elements to find target
target = 999_999
start = time.perf_counter()
found = target in arr
end = time.perf_counter()
print("O(n) search time:", end - start)