import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def func(X):
    F = (X[0]+X[1])**2 + (X[1]+X[2])**2
    return F
def f_con(X):
    G = X[0] + 2.0*X[1] + 3.0*X[2] - 1.0
    return G
x0 = np.array([-4.0, 1.0, 2.0])    
res = optimize.fmin_slsqp(func, x0, f_eqcons=f_con, iter=1000, acc=1e-06, disp=True, full_output=True)


# conz = ({'type': 'eq', 'fun': f_con})
# res2 = optimize.minimize(func, x0, method='L-BFGS-B', constraints=conz, options={'disp': True})