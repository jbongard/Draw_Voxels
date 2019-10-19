import constants as c
import matplotlib.pyplot as plt
import numpy as np

from mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import

from cppn import CPPN
cppn = CPPN()

robot = np.zeros([c.robotResolution,c.robotResolution,c.robotResolution],dtype='f')

cppn.Paint(robot)

# n_voxels = np.random.choice([0,1,2] , size=(20,20,20) , p=[0.99,0.005,0.005])

facecolors = np.where(robot==2, 'salmon', 'lightgreen')
 
fig = plt.figure()

ax = fig.gca(projection='3d')

ax.voxels(robot, facecolors=facecolors , edgecolors = 'k')

#ax.set_axis_off()

#fig.patch.set_facecolor('xkcd:mint green')

#ax.w_xaxis.set_pane_color((0,0,0, 1.0))
#ax.w_yaxis.set_pane_color((0,0,0, 1.0))
#ax.w_zaxis.set_pane_color((0,0,0, 1.0))

plt.show()

