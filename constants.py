import numpy as np

import math

# --------- Evolution -------------------

popSize = 50

numGenerations = 200 

worstFitness = +1000000 # Fitness should always be minimized. 

# ---------------- CPPN -----------------

cppnHiddens = 3

cppnInitialMinWeight = -1.0

cppnInitialMaxWeight = +1.0

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
