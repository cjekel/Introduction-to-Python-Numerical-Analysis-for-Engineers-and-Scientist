from __future__ import print_function
# or integrate(y, (x, -3.25, 7.32))

from sympy import *
from pyDOE import lhs
import matplotlib.pyplot as plt

# ========== HW10 SOLUTION [Python2/3] ========== #


# ========== 1 ========== #

x, y = symbols('x y')
w = 3.0*x**2*y + 2*y + y*sin(x)
ans = w.diff(x)
# or diff(w, x)
print(ans)

# ========== 2 ========== #

y = 3.3*x**6 + 1.7*x**4 - 7.3*x**3 + 6.7*x
ans = y.integrate((x, -3.25, 7.32))
# or integrate(y, (x, -3.25, 7.32))
print(ans)

# ========== 3 ========== #

# option 1

y = 5.0*x**8 + 3.0*x**3 + 3.0*x**2 - 2.5*x + 1.1
ans = solve(y, x)

# option 2

eqn = Eq(5.0*x**8 + 3.0*x**3 + 3.0*x**2 - 2.5*x + 1.1, 0)
ans = solve(eqn, x)

print(ans)

# ========== 4 ========== #

m = Symbol('m')

M = Matrix([[m**2, 2.0*m, 1.0, 2.3],
            [m, 2.3, -5.0, 2.1],
            [2.1, 73.0, -56.0, 1.1],
            [-12.0, -1.0, 13.0, m]])

ans = M.det()
# or det(M)
print(ans)

# optionally, this is how to fix the rounding issue:

M_det_fix = M.det()
for x in postorder_traversal(M.det()):
    if isinstance(x, Float):
        M_det_fix = M_det_fix.subs(x, round(x, 1))

# ========== 5 ========== #

lhd = lhs(2, samples=10, criterion='c')
x_1 = lhd[:,0]
x_2 = lhd[:,1]

plt.figure()
plt.plot(x_1,x_2, 'o')
plt.grid(True)
plt.xlim((0,1))
plt.ylim((0,1))
plt.show()
