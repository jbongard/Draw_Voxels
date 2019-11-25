import sys
sys.path.insert(0, '..')

from   cppn              import CPPN
import numpy             as     np
import matplotlib.pyplot as     plt

cppn = CPPN(inputWidth=2,outputWidth=1)

outputs = np.zeros([50,50],dtype='f')

x = np.linspace(-1.0 , +1.0)

y = np.linspace(-1.0 , +1.0)

for xIndex in range(50):

    for yIndex in range(50):

        outputs[ xIndex , yIndex ] = cppn.Evaluate_At( [ x[xIndex] , y[yIndex] ] )

plt.matshow( outputs )

plt.show()

