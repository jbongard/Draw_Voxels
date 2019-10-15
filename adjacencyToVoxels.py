import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from cppn import CPPN

cppn = CPPN()

robot = np.zeros([2,2,2],dtype='f')

cppn.Paint(robot)

exit()

fig = plt.figure()

ax = fig.gca(projection='3d')

#ax.voxels(np.ones((2,2,2),dtype='d')) , edgecolor='k')

vs = np.random.choice( [0,1] , size=(20,20,20) , p=[0.99, 0.01] )

ax.voxels( vs , edgecolor='k')


plt.show()
