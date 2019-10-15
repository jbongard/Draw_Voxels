from scipy import signal
import numpy as np

in1 = np.ones([1,1],dtype='f')

#kernel = np.zeros([3,3],dtype='f')
#kernel[1,1] = 1
kernel = np.random.choice( [0,1] , size=(3,3) , p=[0.5, 0.5] )


print(in1)

print(kernel)

out = signal.convolve2d(in1, kernel, mode='same', boundary='fill', fillvalue=0)

print(out)
