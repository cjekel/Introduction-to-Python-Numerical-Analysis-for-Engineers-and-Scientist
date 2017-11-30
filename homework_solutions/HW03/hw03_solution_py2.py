from __future__ import print_function

import pyDOE
import os
import math
import numpy as np

# ========== HW03 SOLUTION [Python2] ========== #


# ========== 1 ========== #
# see 2nd import statement at the top of the script file.

# ========== 2 ========== #
# see 3rd import statement at the top of the script file.

# WINDOWS:
print(os.getcwd())
# os.system('ping -n 2 ufl.edu')

# LINUX/MACOS:
# os.system('ping -c 2 ufl.edu')

# ========== 3 ========== #
# see 4th and 5th import statements at the top of the script file.
print(math.pi == np.pi)

# the two are equivalent.

# ========== 4 ========== #
class Sphere:
    def __init__(self, radius, mass):
        self.radius = radius
        self.mass = mass
        self.volume = 4.0 / 3 * math.pi * self.radius ** 3
        self.surface_area = 4.0 * math.pi * self.radius ** 2
        self.density = self.mass / self.volume

red = Sphere(1.7, 0.25)
print(dir(red))
print('volume: {0.volume}\nsurface area: {0.surface_area}\n'
      'density: {0.density}'.format(red))

# ========== 5 ========== #
x = [[0, 1, 2, 3], [4, 5, 6, 7],
     [8, 9, 10, 11], [12, 13, 14, 15]]

# option 1
for l in x:
    print(l[0], l[1], l[2], l[3], sep=' & ')

# option 2 (list unpacking):
for l in x:
    print(*l, sep=' & ')

# option 3 (tuple unpacking):
for a, b, c, d in x:
    print(a, b, c, d, sep=' & ')
