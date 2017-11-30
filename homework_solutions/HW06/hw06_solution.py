import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# ========== HW06 SOLUTION [Python2/3] ========== #


# ========== 1 ========== #

def beale(x1, x2):
    return ((1.5 - x1 * (1 - x2)) ** 2
            + (2.25 - x1 * (1 - x2 ** 2)) ** 2
            + (2.625 - x1 * (1 - x2 ** 3)) ** 2)

x1 = np.linspace(0, 4, 100)
x2 = np.linspace(-0.5, 1, 100)
x1, x2 = np.meshgrid(x1, x2)
f = beale(x1, x2)

# ========== 2 ========== #

plt.figure()
plt.contourf(x1, x2, f, 100, cmap=plt.cm.hot)
plt.colorbar()
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.show()

# ========== 3 ========== #

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.scatter(x1, x2, f, 'ob')
ax.set(xlabel=r'$x_1$',
       ylabel=r'$x_2$',
       zlabel=r'$f(x1, x2)$')
fig.show()

# ========== 4 ========== #

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(x1, x2, f)
ax.set(xlabel=r'$x_1$',
       ylabel=r'$x_2$',
       zlabel=r'$f(x1, x2)$')
fig.show()

# ========== 5 ========== #

a = np.array([3.5, -0.2])
b = np.array([2.0, 0.9])
n_points = 100
lam = np.linspace(0, 1, num=n_points)
x1 = np.linspace(a[0], b[0], num=n_points)
x2 = np.linspace(a[1], b[1], num=n_points)
f = beale(x1, x2)

plt.figure()
plt.plot(lam, f)
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.show()
