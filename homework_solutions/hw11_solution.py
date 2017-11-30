from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# ========== HW11 SOLUTION [Python2/3] ========== #

np.random.seed(1)
x = np.random.random(20) * 2.0
noise = np.random.normal(size=20)
y = 2.0 * x - 3.2 + noise
plt.figure()
plt.plot(x, y, 'o')
plt.show()

X = x.reshape(-1, 1)

# ========== 1 ========== #

linreg_fit = LinearRegression(fit_intercept=True)
linreg_fit.fit(X, y)
print(linreg_fit.score(X, y))

# ========== 2 ========== #

X = x.reshape(-1, 1)

poly2 = PolynomialFeatures(degree=2)
X = poly2.fit_transform(X)
quad_fit = LinearRegression(fit_intercept=False)
quad_fit.fit(X, y)
print(quad_fit.score(X, y))

# ========== 3 ========== #

X = x.reshape(-1, 1)

poly10 = PolynomialFeatures(degree=10)
X = poly10.fit_transform(X)
poly10_fit = LinearRegression(fit_intercept=False)
poly10_fit.fit(X, y)
print(poly10_fit.score(X, y))

# ========== 4 ========== #

# flank the x values
xs = np.linspace(np.min(x) - .5,
                 np.max(x) + .5, 100)
xs = xs.reshape(-1, 1)
xs_quad = poly2.transform(xs)
xs_poly10 = poly10.transform(xs)
lin_yhat = linreg_fit.predict(xs)
quad_yhat = quad_fit.predict(xs_quad)
poly10_yhat = poly10_fit.predict(xs_poly10)

plt.figure()
plt.plot(x, y, 'o')
plt.plot(xs, lin_yhat, '-')
plt.plot(xs, quad_yhat, '-')
plt.plot(xs, poly10_yhat, '-')
plt.show()

# the 10-degree model had the highest r^2,
# but it is clearly overfitting!

# zoom in:

plt.figure()
plt.plot(x, y, 'o')
plt.plot(xs, lin_yhat, '-')
plt.plot(xs, quad_yhat, '-')
plt.plot(xs, poly10_yhat, '-')
plt.xlim(np.min(x), np.max(x))
plt.ylim(np.min(y), np.max(y))
plt.show()
