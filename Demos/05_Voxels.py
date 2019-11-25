import sys
sys.path.insert(0, '..')

from   cppn              import CPPN
import numpy             as     np
import matplotlib.pyplot as     plt

resolution = 10

cppn = CPPN(inputWidth=3,outputWidth=1)

outputs = np.zeros( [resolution , resolution , resolution ] , dtype = 'f' )

x = np.linspace(-1.0 , +1.0 , num = resolution )

y = np.linspace(-1.0 , +1.0 , num = resolution )

z = np.linspace(-1.0 , +1.0 , num = resolution )

for xIndex in range(resolution):

    for yIndex in range(resolution):

        for zIndex in range(resolution):

            output = cppn.Evaluate_At( [ x[xIndex] , y[yIndex] , z[zIndex] ] )

            if output < 0:

                outputs[ xIndex , yIndex , zIndex ] = 0
            else:
                outputs[ xIndex , yIndex , zIndex ] = 1


fig = plt.figure()
ax = fig.gca(projection='3d')
ax.set_aspect('equal')

ax.voxels(outputs, edgecolor="k")

plt.show()
