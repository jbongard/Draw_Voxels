import numpy as np

import math

# --------- Evolution -------------------

popSize = 10

numGenerations = 1000 

# -------------- Robot ------------------

robotResolution = 10

# ---------------- CPPN -----------------

cppnInputs = 4 # x , y , z , bias

cppnHiddens = 3

cppnOutputs = 1 # negative = no voxel; positive = voxel  

cppnInitialMinWeight = -10.0

cppnInitialMaxWeight = +10.0

cppnSinActFn = 0
cppnAbsActFn = 1
cppnGauActFn = 2
cppnTanActFn = 3
cppnNegActFn = 4
cppnIdnActFn = 5

def Gaussian(X):

    return np.exp( -X**2 / 2.0 )

def Negate(X):

    return -1 * X 

def Identity(X):

    return X

cppnActivationFunctions = {}

cppnActivationFunctions[cppnSinActFn] = np.sin

cppnActivationFunctions[cppnAbsActFn] = np.abs

cppnActivationFunctions[cppnGauActFn] = Gaussian

cppnActivationFunctions[cppnTanActFn] = np.tanh

cppnActivationFunctions[cppnNegActFn] = Negate

cppnActivationFunctions[cppnIdnActFn] = Identity

numCPPNActivationFunctions = len(cppnActivationFunctions)
