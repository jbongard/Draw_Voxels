import matplotlib.pyplot as plt

import constants as c

from afpo import AFPO

afpo = AFPO()

afpo.Evolve_At_Resolution(c.robotResolution)

afpo.Save_Best()

#afpo.Show_Best_At_Resolution(c.robotResolution)
#plt.show()

#afpo.Show_Best_At_Resolution(20)
#plt.show()
