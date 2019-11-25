import sys
sys.path.insert(0, '..')

from   cppn          import CPPN
import numpy         as     np

cppn = CPPN(inputWidth=2,outputWidth=1)

for x in np.linspace(-1.0 , +1.0):

    for y in np.linspace(-1.0 , +1.0):

        output = cppn.Evaluate_At( [x,y] )

        print( x , y , output )
