import constants as c

from afpo import AFPO

afpo = AFPO()

afpo.Evolve_At_Resolution(c.robotResolution)

afpo.Show_Best_At_Resolution(c.robotResolution)

#afpo.Show_Best_At_Resolution(20)

afpo.Save_Best()

