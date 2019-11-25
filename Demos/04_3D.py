import sys
sys.path.insert(0, '..')

from   cppn              import CPPN
import numpy             as     np
import matplotlib.pyplot as     plt

cppn = CPPN(inputWidth=3,outputWidth=1)

outputs = np.zeros([50,50,50],dtype='f')

x = np.linspace(-1.0 , +1.0)

y = np.linspace(-1.0 , +1.0)

z = np.linspace(-1.0 , +1.0)

for xIndex in range(50):

    for yIndex in range(50):

        for zIndex in range(50):

            output = cppn.Evaluate_At( [ x[xIndex] , y[yIndex] , z[zIndex] ] )

            if output < 0:

                outputs[ xIndex , yIndex , zIndex ] = 0
            else:
                outputs[ xIndex , yIndex , zIndex ] = 1

print(outputs)
