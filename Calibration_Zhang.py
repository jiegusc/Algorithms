import sympy
import numpy as np
# a, c, u0, b, v0 = sympy.symbols("a, c, u0, b, v0" )
import math
# A = np.mat([[a, c, u0], [0, b, v0], [0, 0, 1]])
# print(np.linalg.pinv(A.T))



a = np.mat([[1,2],[3,4]])
b = np.mat([[1,3], [2,4]])

a_inv = a.I
b_inv = b.I

su = a_inv * b_inv

dd = b* a
dd_inv = dd.I

print("su : " ,su)
print("dd_inv: ", dd_inv)

a = Gaussian