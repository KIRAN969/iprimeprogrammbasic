import collections
x=collections.deque([1,5,4,9])
x.append(6)
x.appendleft(6)
x.pop()
x.popleft()
del x[2]
print(x)