import numpy as np
import matplotlib.pyplot as plt
from scipy import optimize

def func(X):
    F = (X[0]+X[1])**2 + (X[1]+X[2])**2
    return F
def f_con1(X):
    G = X[0] + 2.0*X[1] + 3.0*X[2] - 1.0
    return G, -G
# def f_con2(X):
#     G = X[0] + 2.0*X[1] + 3.0*X[2] - 1.0
#     return -G
x0 = np.array([-4.0, 1.0, 2.0])    
res = optimize.fmin_slsqp(func, x0, f_ieqcons=f_con1, iter=1000, acc=1e-06, disp=True, full_output=True)