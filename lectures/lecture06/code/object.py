import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0, 2.0*np.pi, 25)

# the figure and axes of the plot are now objects
fig, ax = plt.subplots()

# you plot on the axes
ax.plot(x,np.cos(x), '--o', label='cos')
ax.plot(x,np.sin(x), '-.s', label='sin')
ax.grid(True)
ax.legend()
# However these labels are different!
ax.set_xlabel('x axis')
ax.set_ylabel('y axis')

fig.show()

# ax.savefig('my_fig.pdf', dpi=600, format='pdf',
             # bbox_inches='tight')


import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(0.0, 2.0*np.pi, 25)
fig, ax = plt.subplots()
ax.plot(x,np.cos(x), '--o', label='cos')
ax.plot(x,np.sin(x), '-.s', label='sin')
ax.grid(True)
ax.legend()

# using set to set multiple items
ax.set(xlim=(-1,7), ylim=(-2,2), 
    xlabel='x', ylabel='y', 
    title='cos and sin plot')

fig.show()