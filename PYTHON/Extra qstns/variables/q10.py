"""
Demonstrate that Python variables are references, not containers.
"""

a = [1, 2, 3]
b = a
b.append(4)
print(a)  # [1, 2, 3, 4] — same list!
c = a.copy()
c.append(5)
print(a)  # [1, 2, 3, 4] — not changed