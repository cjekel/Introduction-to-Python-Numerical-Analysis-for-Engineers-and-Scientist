import numpy as np
import matplotlib.pyplot as plt
a = np.array([0.33, .57])
b = np.array([-0.11, -0.2])
u = b-a #
lam = np.linspace(0,1,100)
x = np.zeros(100)
y = np.zeros(100)
for i,j in enumerate(lam):
    r = (a + (j*u))
    x[i] = r[0]
    y[i] = r[1]
F = (1.0-x)**2 + (100.0*((y-(x**2))**2))
plt.figure()
plt.plot(lam,F)
plt.ylabel('F'); plt.xlabel(r'$\lambda$')
plt.show()