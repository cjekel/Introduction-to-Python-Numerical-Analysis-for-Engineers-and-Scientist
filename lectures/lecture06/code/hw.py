import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(0,4,100)
x2 = np.linspace(-0.5,1,100)

x1, x2 = np.meshgrid(x1,x2)
f = (1.5 - x1*(1.0-x2))**2 + (2.25 - x1*(1.0-(x2**2)))**2 + (2.625 - x1*(1.0-(x2**3)))**2

plt.figure()
plt.contourf(x1,x2,f,100)
plt.colorbar()
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.show()