from afpo import AFPO

import sys

randomSeed = int(sys.argv[1])

afpo = AFPO(randomSeed)

afpo.Evolve()

afpo.Show_Best_Genome()
