from collections import deque

list1 = deque()
for i in range(10):
    list1.appendleft(i)

print(list1)
print(list1[0])

list1.popleft()
print(list1)
