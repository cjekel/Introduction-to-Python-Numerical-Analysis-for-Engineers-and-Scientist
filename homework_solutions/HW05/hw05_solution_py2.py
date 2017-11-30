import numpy as np
import matplotlib.pyplot as plt

# ========== HW04 SOLUTION [Python2] ========== #


# ========== 1 ========== #

five_dim_array = np.load('five_dim_array.npy')
array_flat = five_dim_array.flatten()
print array_flat.argmin()

# ========== 2 ========== #

x = np.linspace(-10, 10)

plt.figure()
plt.plot(x, 1 / x, label=r'$f(x) = \frac{1}{x}$')
plt.plot(x, x, label=r'$g(x) = x$')
plt.plot(x, x ** 2, label=r'$h(x) = x^2$')
plt.plot(x, x ** 3, label=r'$k(x) = x^3$')
plt.legend()
plt.show()

# ========== 3 ========== #

x = np.linspace(-1, 4, num=50)
y = 3.7 * x ** 2 - 7.0 * x + 3.1
noise = np.random.normal(0, 5, size=50)

plt.figure()
plt.plot(x, y + noise, label=r'$f(x) = 3.72x^2-7.0x+3.1 + \epsilon$')
plt.plot(x, y, label=r'$f(x) = 3.72x^2-7.0x+3.1$')
plt.grid(True)
plt.xlabel('x')
plt.ylabel('f(x)')
plt.show()
