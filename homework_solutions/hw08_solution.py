from __future__ import print_function

import numpy as np
from scipy import optimize

# ========== HW08 SOLUTION [Python2/3] ========== #


# ========== 1 ========== #

def func(x):
    h, w, d = x
    return 2.0 * (w*h + d*h + 2*w*d)


def f_con(x):
    h, w, d = x
    g = 2.0 - h*d*w
    return -g

bounds = ((0, None),) * 3
x0 = np.array([1.0] * 3)

res = optimize.fmin_slsqp(func, x0, f_ieqcons=f_con, bounds=bounds, full_output=True)

H, W, D = res[0]
print('H: {}\nW: {}\nD: {}'.format(H, W, D))
print('SA:', res[1])
print('V:', H*W*D)

# ========== 2 ========== #

def woods(x):
    #   Woods function
    a = 100.0 * ((x[1] - (x[0]**2))**2)
    b = (1.0 - x[0])**2
    c = 90.0 * ((x[3] - (x[2]**2))**2)
    d = (1.0 - x[2])**2
    e = 10.0 * ((x[1] + x[3] - 2.0)**2)
    f = 0.1 * ((x[1] - x[3])**2)
    return a + b + c + d + e + f

bounds = ((-10.0, 10.0),) * 4

# option 1: differential evolution (preferred)

res = optimize.differential_evolution(woods, bounds, maxiter=1000)
print(res.x)
print(res.fun)

# option 2: SLSQP

x0 = np.zeros(4)
res = optimize.fmin_slsqp(woods, x0, bounds=bounds, full_output=True)
print(res[0])
print(res[1])
