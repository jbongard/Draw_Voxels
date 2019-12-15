from afpo import AFPO

import sys

randomSeed = int(sys.argv[1])

dimensionality = int(sys.argv[2])

afpo = AFPO(randomSeed,dimensionality)

afpo.Evolve()

afpo.Show_Best_Genome()
