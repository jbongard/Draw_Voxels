import numpy as np

import math

# --------- Evolution -------------------

popSize = 10

numGenerations = 20

worstFitness = +1000000 # Fitness should always be minimized. 

# ---------- Robots ---------------------

robotResolution = 12

voxelLength = 2.0 / (robotResolution-1)
