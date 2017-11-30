import numpy as np
import matplotlib.pyplot as plt
# Create some normally distributed data        
mean = [0, 1]        
cov = [[1, 1], [1, 2]]        
x, y = np.random.multivariate_normal(mean, cov, 3000).T
# Set up the axes with gridspec        
fig = plt.figure(figsize=(6, 6))        
grid = plt.GridSpec(4, 4, hspace=0.2, wspace=0.2)        
main_ax = fig.add_subplot(grid[:-1, 1:])        
y_hist = fig.add_subplot(grid[:-1, 0], sharey=main_ax)        
x_hist = fig.add_subplot(grid[-1, 1:], sharex=main_ax)
        
# scatter points on the main axes        
main_ax.plot(x, y, 'x')
main_ax.grid(True)
# histogram on the attached axes        
x_hist.hist(x, 40, orientation='vertical',
 edgecolor='black')        
x_hist.invert_yaxis()
y_hist.hist(y, 40, orientation='horizontal',
 edgecolor='black')        
y_hist.invert_xaxis()
fig.show()