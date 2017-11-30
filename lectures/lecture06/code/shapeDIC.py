#    -*- coding: utf-8 -*-

# Created by Charles Jekel in 2015
# Please request permission before use
# and cite http://scholar.sun.ac.za/handle/10019.1/98627
#
# cjekel@gmail.com or cj@jekel.me
#
#   Import the necessary packages
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle, Wedge, Polygon, Circle



fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

#   Camera lens rays
ax.add_patch(Polygon(np.array([[24.035,-9.133],[33,-47.5],[80,-47.5],[25.7182,-7.73303]]),closed=True,ls='dashed',fc='#99ccff'))

dic = Rectangle((0, 0), 100, 10, fc='none')
ax.add_patch(dic)
ax.text(50,5, 'DIC System', ha='center', va='center',fontsize=16)
bbox_props = dict(boxstyle="rarrow,pad=0.3", fc="cyan", ec="b", lw=2)

#   Camera lens rays
ax.add_patch(Polygon(np.array([[24,-9],[33,-47.5],[80,-47.5],[25,-7.2]]),closed=True,ls='dashed',fc='#CCE6FF'))
ax.add_patch(Polygon(np.array([[73.9481,-7.45807],[20,-47.5],[67,-47.5],[76.1553,-9.29489]]),closed=True,ls='dashed',fc='#CCE6FF'))
ax.add_patch(Polygon(np.array([[24,-9],[33,-47.5],[80,-47.5],[25,-7.2]]),closed=True,ls='dashed',fc='none', ec='black'))
ax.add_patch(Polygon(np.array([[73.9481,-7.45807],[20,-47.5],[67,-47.5],[76.1553,-9.29489]]),closed=True,ls='dashed',fc='none', ec='black'))


#   Cameras
c1 = Rectangle((20, -10.0), 10, 20, angle=40.0, fc='k')
c2 = Rectangle((80, -10.0), 20, 10, angle=50.0, fc='k')
c1l = Rectangle((23, -10.0), 5, 2, angle=40.0, fc='k')
c2l = Rectangle((77, -10), 2, 5, angle=50.0, fc='k')

a = Rectangle.get_patch_transform(c1)
print Rectangle.get_path(c1)
ax.add_patch(c1)
ax.add_patch(c1l)

ax.add_patch(c2)
ax.add_patch(c2l)




#   Supports
ax.add_patch(Rectangle((20, -50.), 15, 2.5, fc='White', ec='Black'))#, hatch='\\'))
ax.add_patch(Rectangle((65, -50.), 15, 2.5, fc='White', ec='Black'))#, hatch='\\'))
#   bottom left
ax.add_patch(Rectangle((20, -55), 26.5, 5, fc='White', ec='Black'))#, hatch='/'))
#   bottom mid
ax.add_patch(Rectangle((47.5, -55), 5, 5, fc='White', ec='Black'))#, hatch='/'))
#   bottom right
ax.add_patch(Rectangle((53.5, -55), 26.5, 5, fc='White', ec='Black'))#, hatch='/'))


ax.annotate('Pressure Sensor', xy=(47, -55), xytext=(47, -65),arrowprops=dict(facecolor='black', width=1,headwidth=5,shrink=0.02),horizontalalignment='right', verticalalignment='top')
ax.annotate('Line Pressure', xy=(53, -55), xytext=(53, -65),arrowprops=dict(facecolor='black', width=1,headwidth=5,shrink=0.02),horizontalalignment='left', verticalalignment='top')

ax.annotate('Test\nFixture', xy=(25, -47.5), xytext=(15, -30),arrowprops=dict(facecolor='black', width=1,headwidth=5,shrink=0.02),horizontalalignment='center', verticalalignment='top')


#   Bubble
ax.add_patch(Wedge((50, -50), 15, 0, 180, fc='blue'))
ax.annotate('Inflated\nMaterial', xy=(63.3, -43.6), xytext=(85, -20.6),arrowprops=dict(facecolor='black', width=1,headwidth=5,shrink=0.02),horizontalalignment='center', verticalalignment='top')


ax.axis('off')
ax.axes.set_xlim([-5,105])
ax.axes.set_ylim([-75,20])

plt.show()
plt.savefig('dicOutline.pdf', format='pdf', dpi=1200, bbox_inches='tight')
