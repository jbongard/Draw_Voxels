from scipy import signal
import numpy as np

#kernel = np.ones([1,1],dtype='f')
kernel = [0,1]

matrix = np.random.choice( [0,1] , size=(3,3) , p=[0.5, 0.5] )

print(kernel)

print(matrix)

out = signal.convolve(kernel, matrix, mode='same', boundary='fill', fillvalue=0)

print(out)
