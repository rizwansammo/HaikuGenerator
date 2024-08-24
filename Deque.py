from collections import deque

dq = deque()

# Adding elements to both ends
dq.append(1)
dq.append(2)
dq.appendleft(0)
dq.append(3)

# Removing elements from both ends
print(dq.pop())      # Output: 3
print(dq.popleft())  # Output: 0

# Accessing elements
print(dq[0])  # Output: 1

# Output:
# deque([1, 2])
