# def bs (a, x):
#     lo, hi = 0, len(a) - 1
#     while lo <= hi:
#         mid = (lo + hi) // 2
#         if a[mid] == x: lo = hi = mid
#         if a[mid] < x: lo = mid + 1
#     else: hi = mid - 1
#     return lo if a[lo] == x else -1

# arr = [5, 2, 4]
# arr. sort()
# print(arr)

# words = ["apple", "fig", "banana"]
# print(sorted(words, key=len))

# count = 0
# for i in range(3):
#     for j in range(2):
#      count += 1
#      print(count)

# class Node:
# def __init__(self, value):
#         self.data = value
#         self.next = None
# a = Node(10)
# b = Node(20)
# a.next = b
# print(a. next.value)  # Output: 20

# class Node:
#     def __init__(self, v, next =None):
#         self.v = self.next = v, next
# head = Node(1, Node(2, Node (3)))
# head = head.next
# print(head. v)

# import heapq
# h = [5, 1, 4,]
# heapq.heapify(h)
# print(heapq.heappop(h))  # Output: 1

# soon = {}
# for x in(2, 3, 2):
#     soon[x] = soon. get (x, 0) + 1
# print(soon[2])

# nums = [2, 7, 11]
# target = 9
# seen = set()
# for x in nums:
#     if target -x in seen:
#         print(x)
#         break
#     seen.add(x)

