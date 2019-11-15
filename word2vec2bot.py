import matplotlib.pyplot as plt

import constants as c

from afpo import AFPO

import sys

arguments = len(sys.argv) - 1

randomSeed = int(sys.argv[arguments])

afpo = AFPO(randomSeed)

afpo.Evolve_At_Resolution(c.robotResolution)

#afpo.Show_Best_At_Resolution(c.robotResolution)
#plt.show()

#afpo.Show_Best_At_Resolution(20)
#plt.show()
