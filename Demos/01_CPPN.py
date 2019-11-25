import sys
sys.path.insert(0, '..')

from   cppn          import CPPN

cppn = CPPN(inputWidth=2,outputWidth=1)

x = 0
y = 0

output = cppn.Evaluate_At( [x,y] )

print(output)
