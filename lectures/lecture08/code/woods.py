import numpy as np
from scipy import optimize
def woods(var):
    #   Woods function
    a = 100.0*((var[1]-(var[0]**2))**2)
    b = (1.0-var[0])**2
    c = 90.0*((var[3]-(var[2]**2))**2)
    d = (1.0-var[2])**2
    e = 10.0*((var[1]+var[3] -2.0)**2)
    f = 0.1*((var[1]-var[3])**2)
    return a + b + c + d + e + f
bounds = np.ones([4,2])
bounds[:,0] *= -10.0
bounds[:,1] *= 10.0
res = optimize.differential_evolution(woods, bounds, args=(), strategy='best1bin', 
     maxiter=1000, popsize=15, tol=0.01, mutation=(0.5, 1), recombination=0.7, 
     seed=None, callback=None, disp=True, polish=True, 
     init='latinhypercube', atol=0)