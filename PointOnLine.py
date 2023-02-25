import numpy as np
import version_information
import matplotlib.pyplot as plt



class point:
    def __init__(self):
        self.x = 0
        self.y = 0

a = point()
a.x = 0
a.y= 0

b = point()
b.x = 5
b.y = 2

c = point()
c.x = 3
c.y = 5


def perpDotProduct(a, b, c):
    return (a.x - c.x) * (b.y - c.y) - (a.y - c.y) * (b.x - c.x)


print(perpDotProduct(a,b,c))

a1 = np.array([5,2])
a2 = np.array([3,5])
print(np.cross(a1, a2))

print(np.dot(np.array([4,3]),np.array([4,3])))


"""
Get projected point P' of P on line e1. Faster version.
@return projected point p.
"""

p1 = point()
p1.x = 4
p1.y= 4

p2 = point()
p2.x = 8
p2.y= 8

given_p = point()
given_p.x = 7
given_p.y = 8
"""
p1: start point
p2: end point
"""

def getProjectedPointOnLineFast(p1, p2, given_p):
  # get dot product of e1, e2 vectors
    e1 = point()
    e1.x, e1.y = p2.x - p1.x, p2.y - p1.y
    e2 = point()
    e2.x, e2.y = given_p.x - p1.x, given_p.y - p1.y
    np_e1, np_e2  = np.array([e1.x, e1.y]), np.array([e2.x, e2.y])
  # get squared length of e1

    valDp = np.dot(np_e1, np_e2)
    len1 = e1.x * e1.x + e1.y * e1.y
    p = point()
    p.x, p.y = p1.x + (valDp * e1.x) / len1, p1.y + (valDp * e1.y) / len1
    return p

g = getProjectedPointOnLineFast(p1, p2, given_p)

#
# %reload_ext version_information
# print(version_information numpy)

data = np.random.normal(size=(15,15))

arr = np.arange(-100, 101, 1)/10
print(len(arr))
y = np.log(arr/ (1 - arr))
print(y)
# print(np.log(0.4 / (1 - 0.4)))

y2 = 1 / (1 + np.exp(-arr))
plt.plot(arr,y2)
plt.show()