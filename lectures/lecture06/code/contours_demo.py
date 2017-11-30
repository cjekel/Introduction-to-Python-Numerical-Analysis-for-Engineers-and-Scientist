import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
x = np.linspace(-2,2,100)
y = np.linspace(-1,3,100)
#x,y = np.meshgrid(x,y)
f = (1.0-x)**2 + (100.0*((y-(x**2))**2))
# plt.figure()
# plt.plot(x,y,'ok')
# plt.show()
plt.figure()
plt.contourf(x,y,f,100)
plt.colorbar()

x,y = np.meshgrid(x,y)
f = (1.0-x)**2 + (100.0*((y-(x**2))**2))

plt.figure()
plt.contourf(x,y,f,100)
plt.colorbar()
plt.show()

# 
# plt.figure()
# levels=[0, 1, 5, 10, 100, 500, 1000, 2000]
# plt.contourf(x,y,f,levels)
# plt.colorbar()
# plt.show()

#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
#ax.scatter(x,y, f, 'ob')
#ax.set( xlabel='X Label', ylabel ='Y Label', zlabel='Z Label')
#fig.show()
