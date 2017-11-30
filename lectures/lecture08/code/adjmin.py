import numpy as np
from scipy import optimize
import matplotlib.pyplot as plt


def adjiman(x):
    F = np.cos(x[0])*np.sin(x[1]) - ((x[0])/(x[1]**2 +1.0))
    return F
    
# optimization bounds 
bounds = ((-10.0,10.0),
          (-10.0,10.0))    
# run differential evolution          
res = optimize.differential_evolution(adjiman, bounds, maxiter=1000, popsize=50, disp=True)

# this l bfgs b won't find the optimum
res2 = optimize.fmin_l_bfgs_b(adjiman, (-2,-2), approx_grad=True, bounds=bounds)

# hower this l bfgs b will
res3 = optimize.fmin_l_bfgs_b(adjiman, (2,2), approx_grad=True, bounds=bounds)

x0 = np.linspace(-10,10,100)
x1 = np.linspace(-10,10,100)
x0, x1 = np.meshgrid(x0,x1)

F = adjiman((x0,x1))

plt.figure()
plt.contourf(x0,x1,F)
plt.colorbar()
plt.show()