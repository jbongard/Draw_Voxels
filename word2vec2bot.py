from afpo import AFPO

import sys

arguments = len(sys.argv) - 1

randomSeed = int(sys.argv[arguments])

afpo = AFPO(randomSeed)

afpo.Evolve()
