import sys
sys.path.insert(0, '..')

from   cppn              import CPPN
import numpy             as     np
import math
import matplotlib.pyplot as     plt
import copy

resolutionIncreases = 4 * 4 

panelWidth = math.sqrt(resolutionIncreases)

# ------------------ Functions --------------------

def Create_Random_CPPN():

    return CPPN(inputWidth=3,outputWidth=1)

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

def Draw_Tensor(panelIndex,tensor):

    fig = plt.figure( 1 )

    ax = fig.add_subplot( panelWidth , panelWidth , panelIndex, projection='3d')
    ax.set_aspect('equal')
    ax.voxels( tensor , edgecolor="k")

# ---------------- Main function ------------------


parent = Create_Random_CPPN()

for resolution in range(1,resolutionIncreases+1):

    x = np.linspace(-1.0 , +1.0 , num = resolution )
    y = np.linspace(-1.0 , +1.0 , num = resolution )
    z = np.linspace(-1.0 , +1.0 , num = resolution )

    parentTensor = Create_Tensor(parent)

    Draw_Tensor(resolution,parentTensor)

plt.show()
