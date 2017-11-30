from __future__ import print_function
from __future__ import division
import numpy as np
from time import time

x = np.random.random(100000)
# xx = np.array(x)
y = []
t0 = time()
for i in x:
    y.append(2.0*i)
t1 = time()
y = 2.0*x
t2 = time()

print('numpy', t2-t1)
print('for loop', t1-t0)


x = np.ones(10, dtype='int')
y = np.random.random(10)
for i in range(10):
    x[i] = y[i]/2.0