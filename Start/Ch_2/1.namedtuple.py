# Demonstrate the usage of namdtuple objects

import collections


# TODO: create a Point namedtuple
Point = collections.namedtuple("Point", "x y")
p1 = Point(10,20)
print(f"New named tuple point is created: {p1}")
print(f"the named tuple-Point has X-axis:{p1.x} and Y-axis:{p1.y}")
# TODO: use _replace to create a new instance
p2 = p1._replace(x=30)
print(f"New named tuple point is created: {p2} by replacing {p1} with X-axis value:{p2.x}")