# deque objects are like double-ended queues

from collections import deque
import string


# TODO: initialize a deque with lowercase letters
dq = deque(string.ascii_lowercase)
print(dq)

# TODO: deques support the len() function
print(len(dq))

# TODO: deques can be iterated over
for elem in dq:
    print(elem.capitalize())

# TODO: manipulate items from either end
dq.pop()
dq.popleft()
dq.append('1')
dq.appendleft('2')
print(dq)


# TODO: use an index to get a particular item
dq.rotate(3)
print(dq)
dq.rotate(-2)
print(dq)
print(f'getting 7th item in current dq:')
dq.rotate(-7)
print(dq.pop())