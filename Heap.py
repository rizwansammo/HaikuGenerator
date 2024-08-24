import heapq

min_heap = []

# Adding elements
heapq.heappush(min_heap, 5)
heapq.heappush(min_heap, 3)
heapq.heappush(min_heap, 8)
heapq.heappush(min_heap, 1)

# Removing the smallest element
print(heapq.heappop(min_heap))  # Output: 1

# Peeking at the smallest element
print(min_heap[0])  # Output: 3
