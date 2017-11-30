# -*- coding: utf-8 -*-
# Code source: Gaël Varoquaux
#              Andreas Müller
# Modified for documentation by Jaques Grobler
# License: BSD 3 clause

import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_moons, make_circles, make_classification


h = .02  # step size in the mesh



X, y = make_classification(n_features=2, n_redundant=0, n_informative=2,
                           random_state=1, n_clusters_per_class=1)
rng = np.random.RandomState(2)
X += 2 * rng.uniform(size=X.shape)
linearly_separable = (X, y)

datasets = [make_moons(noise=0.3, random_state=0),
            make_circles(noise=0.2, factor=0.5, random_state=1),
            linearly_separable
            ]

for ds_cnt, ds in enumerate(datasets):
    # preprocess dataset, split into training and test part
    X, y = ds
    plt.figure()
    for i,j in enumerate(y):
        if j == 0:
            plt.plot(X[i][0], X[i][1], 'ob')
        else:
            plt.plot(X[i][0], X[i][1], 'xr')
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.title(r'What $f(x_1, x_2)$ sepeates the data?')
    plt.show()



x = np.linspace(0,10,100)
y = 2.0*x -2.0

yNoise = y + np.random.normal(size=100)

plt.figure()
plt.plot(x,yNoise,'o')
plt.plot(x,y,'-')
plt.xlabel('$x$')
plt.ylabel('$f(x)$')
plt.show()

#   let's see how well a gaussian process can fit the data
from sklearn import gaussian_process
import numpy as np
import matplotlib.pyplot as plt

#   full X range
X = np.arange(0.0,10.0+.1,.1)
#   true function values
Y = (X*(np.sin(X)**3)) - (np.cos(X)/(X+.5))

#   let's pick 12 points for the training set
x = np.array([0.5, 0.87, 1.5, 2.8, 3.6, 4.8, 6.5, 6.8, 7.7, 8.4, 9.3, 9.7])
y = (x*(np.sin(x)**3)) - (np.cos(x)/(x+.5))

#   reshape numpy arrays for scikit-learn input 
X = X.reshape(-1,1)
Y = Y.reshape(-1,1)
x = x.reshape(-1,1)
y = y.reshape(-1,1)

gp = gaussian_process.GaussianProcess(corr='cubic')
gp.fit(x,y)
yPred, predMSE = gp.predict(X, eval_MSE=True)



#   plot X and Y
plt.figure()
plt.plot(X,Y, '-k', label=r'$Y = X \sin (X)^3 + \frac{\cos(X)}{X+0.5}$')
plt.plot(x,y, 'ok', label='Training points')
plt.plot(X, yPred, '-r', label='GP prediction')
plt.xlabel('X')
plt.ylabel('Y')
plt.grid(True)
plt.legend(loc =2)
plt.show()
# plt.savefig('Kriging.pdf')



x1 = np.random.random(20)
y1 = np.random.normal(loc=0.5,size=20)
x2 = np.random.random(20)-3.0
y2 = np.random.normal(loc=0.5,size=20)
x3 = np.random.random(20)-5.0
y3 = np.random.normal(loc=0.5,size=20)-5.0
x4 = np.random.random(20)-1.0
y4 = np.random.normal(loc=0.5,size=20)-7.0
plt.figure()
plt.plot(x1,y1,'ok')
plt.plot(x2,y2,'ok')
plt.plot(x3,y3,'ok')
plt.plot(x4,y4,'ok')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.show()
plt.savefig('clust.pdf')


plt.figure()
plt.plot(x1,y1,'or')
plt.plot(x2,y2,'xb')
plt.plot(x3,y3,'^', color='orange')
plt.plot(x4,y4,'D', color='purple')
plt.xlabel(r'$x_1$')
plt.ylabel(r'$x_2$')
plt.show()
plt.savefig('cluster.pdf')