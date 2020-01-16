from mpl_toolkits.mplot3d import Axes3D
import numpy as np
from matplotlib import pyplot as plt
 
fig = plt.figure()
ax = Axes3D(fig)
x1 = np.arange( -2*np.pi, 2*np.pi, 0.1 )
x2 = np.arange( -2*np.pi, 2*np.pi, 0.1 )
X, Y = np.meshgrid(x1, x2)
Z = np.power( X, 2 ) + np.power( Y, 2 )
plt.xlabel('x1')
plt.ylabel('x2')
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='rainbow')
plt.show()