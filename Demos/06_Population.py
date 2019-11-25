import sys
sys.path.insert(0, '..')

from   cppn              import CPPN
import numpy             as     np
import matplotlib.pyplot as     plt

resolution     = 10
populationSize = 2

x = np.linspace(-1.0 , +1.0 , num = resolution )
y = np.linspace(-1.0 , +1.0 , num = resolution )
z = np.linspace(-1.0 , +1.0 , num = resolution )

# ------------------ Functions --------------------

def Create_Population():

    cppns = {}

    for cppn in range(populationSize):

        cppns[cppn] = CPPN(inputWidth=3,outputWidth=1)

    return cppns

def Create_Tensors(cppns):

    tensors = {}

    for cppn in cppns:

        tensors[cppn] = Create_Tensor( cppns[cppn] )

    return tensors

def Create_Tensor( cppn ):

    tensor = np.zeros( [resolution , resolution , resolution ] , dtype = 'f' )

    for xIndex in range(resolution):

        for yIndex in range(resolution):

            for zIndex in range(resolution):

                output = cppn.Evaluate_At( [ x[xIndex] , y[yIndex] , z[zIndex] ] )

                if output < 0:

                    tensor[ xIndex , yIndex , zIndex ] = 0
                else:
                    tensor[ xIndex , yIndex , zIndex ] = 1

    return tensor

# ---------------- Main function ------------------

cppns = Create_Population()

tensors = Create_Tensors(cppns)

for tensor in tensors:

    fig = plt.figure( tensor )
    ax = fig.gca(projection='3d')
    ax.set_aspect('equal')

    ax.voxels( tensors[tensor] , edgecolor="k")

plt.show()
