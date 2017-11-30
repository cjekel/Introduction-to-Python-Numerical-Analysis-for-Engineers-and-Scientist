import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize


# lets just generate some data from known beta parameters
x = np.linspace(0,10,30)
beta0 = 2.7
beta1 = 1.3
y = (beta0*x)/(beta1+x)



# determine beta0 and beta1 by minimizing the mean abs residual error

def my_func(X):
    yHat = (X[0]*x)/(X[1]+x)
    resid = yHat - y
    return np.mean(np.abs(resid))
     
res = optimize.fmin_bfgs(my_func, [3.0, 3.0], full_output=True) 

plt.figure()
plt.plot(x,y,'o')
beta = res[0]
plt.plot(x,(beta[0]*x)/(beta[1]+x))
plt.show()