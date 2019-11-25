import sys
sys.path.insert(0, '..')

from   cppn              import CPPN
import numpy             as     np
import matplotlib.pyplot as     plt
import copy

resolution          = 10
populationSize      = 2 
numberOfGenerations = 5

x = np.linspace(-1.0 , +1.0 , num = resolution )
y = np.linspace(-1.0 , +1.0 , num = resolution )
z = np.linspace(-1.0 , +1.0 , num = resolution )

# ------------------ Functions --------------------

def Compute_Fitness_Of(tensor):

    return np.sum( tensor )

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

def Draw_Tensor_Pair(parentTensor,childTensor):

    fig = plt.figure( generation )

    ax = fig.add_subplot(1, 2, 1, projection='3d')
    ax.set_title('Parent')
    ax.set_aspect('equal')
    ax.voxels( parentTensor , edgecolor="k")

    ax = fig.add_subplot(1, 2, 2, projection='3d')
    ax.set_title('Child')
    ax.set_aspect('equal')
    ax.voxels( childTensor , edgecolor="k")

    plt.show()

# ---------------- Main function ------------------

parent = Create_Random_CPPN()

parentTensor = Create_Tensor(parent)

parentFitness = Compute_Fitness_Of(parentTensor)

for generation in range(1,numberOfGenerations):

    child = copy.deepcopy(parent)

    child.Mutate()

    childTensor = Create_Tensor(child)

    childFitness = Compute_Fitness_Of(childTensor)

    print(parentFitness , childFitness)

    Draw_Tensor_Pair(parentTensor,childTensor)

    if childFitness > parentFitness:

        parent = child

        parentFitness = childFitness

        parentTensor = childTensor

plt.show()
