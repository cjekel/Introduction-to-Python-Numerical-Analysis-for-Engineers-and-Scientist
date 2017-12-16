from __future__ import print_function

import numpy as np
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.model_selection import cross_validate
from sklearn.model_selection import KFold

# ========== HW12 SOLUTION [Python2/3] ========== #

np.random.seed(1)
x = np.random.random(20) * 2.0
noise = np.random.normal(size=20)
y = 2.0 * x - 3.2 + noise
# plt.figure()
# plt.plot(x, y, 'o')
# plt.show()
X = x.reshape(-1, 1)

# linear model
linreg_fit = LinearRegression(fit_intercept=True)

# polynomial model (degree=2)
poly2 = PolynomialFeatures(degree=2)
X_poly2 = poly2.fit_transform(X)
poly2_fit = LinearRegression(fit_intercept=False)

# polynomial model (degree=10)
poly10 = PolynomialFeatures(degree=10)
X_poly10 = poly10.fit_transform(X)
poly10_fit = LinearRegression(fit_intercept=False)


# option 1: one loop for everything (faster)

# for plotting purposes
x_linspace = np.linspace(np.min(X), np.max(X), 100)
X_linspace = x_linspace.reshape(-1, 1)
X_linspace_poly2 = poly2.transform(X_linspace)
X_linspace_poly10 = poly10.transform(X_linspace)

scores_linreg_fit = []
scores_poly2_fit = []
scores_poly10_fit = []
kf = KFold(n_splits=5)
for train, test in kf.split(X):
    X_test, X_train = X[test], X[train]
    y_test, y_train = y[test], y[train]

    # subset training data
    X_lin_train = X[train]
    X_poly2_train = X_poly2[train]
    X_poly10_train = X_poly10[train]

    # subset testing data
    X_lin_test = X[test]
    X_poly2_test = X_poly2[test]
    X_poly10_test = X_poly10[test]

    # fit models
    linreg_fit.fit(X_lin_train, y_train)
    poly2_fit.fit(X_poly2_train, y_train)
    poly10_fit.fit(X_poly10_train, y_train)

    # predict models for plots
    y_hat_lin = linreg_fit.predict(X_linspace)
    y_hat_poly2 = poly2_fit.predict(X_linspace_poly2)
    y_hat_poly10 = poly10_fit.predict(X_linspace_poly10)

    # compute R^2 scores and append to lists
    lin_score = linreg_fit.score(X_lin_test, y_test)
    scores_linreg_fit.append(lin_score)

    poly2_score = poly2_fit.score(X_poly2_test, y_test)
    scores_poly2_fit.append(poly2_score)

    poly10_score = poly10_fit.score(X_poly10_test, y_test)
    scores_poly10_fit.append(poly10_score)

    # uncomment to show visualization for each cross-validation step
    # plt.figure()
    # plt.plot(X_train, y_train, 'ok', label='train')
    # plt.plot(X_test, y_test, 'xb', label='test')
    # plt.plot(X_linspace, y_hat_lin, '.-', label='Linear model')
    # plt.plot(X_linspace, y_hat_poly2, '.-', label='Quadratic model')
    # plt.plot(X_linspace, y_hat_poly10, '.-', label='10 degree model')
    # plt.ylim((-10, 10))
    # plt.legend()
    # plt.show()

print(np.mean(scores_linreg_fit))
print(np.mean(scores_poly2_fit))
print(np.mean(scores_poly10_fit))

# option 2: one-liner for each model (more readable)

scores_linreg_fit = cross_validate(linreg_fit, X, y, cv=5,
                                   return_train_score=False)
scores_poly2_fit = cross_validate(poly2_fit, X_poly2, y, cv=5,
                                  return_train_score=False)
scores_poly10_fit = cross_validate(poly10_fit, X_poly10, y, cv=5,
                                   return_train_score=False)

print(np.mean(scores_linreg_fit['test_score']))
print(np.mean(scores_poly2_fit['test_score']))
print(np.mean(scores_poly10_fit['test_score']))
