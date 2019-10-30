import numpy as np

import math

# ------------- Words -------------------

words = ["jump", "walk", "grab", "encompass"]

numWords = len(words)

# --------- Evolution -------------------

popSize = 50

numGenerations = 1000

worstFitness = -1000000

# -------------- Robot ------------------

robotResolution = 2 * 2 # Must be even

# ---------------- CPPN -----------------

cppnInputs = 5 # x , y , z , d , bias

cppnHiddens = 3

cppnOutputs = 2 # neg/pos = absent/present neg/pos = phase=0/phase=pi 

cppnInitialMinWeight = -10.0

cppnInitialMaxWeight = +10.0

cppnInitialMinW2VWeight = cppnInitialMinWeight / 100.0

cppnInitialMaxW2VWeight = cppnInitialMaxWeight / 100.0

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
