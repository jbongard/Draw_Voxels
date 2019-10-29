import constants as c
import matplotlib.pyplot as plt
import pickle

cppn = pickle.load( open( "data/cppn.p", "rb" ) )

cppn.Add_W2V_Weights()

cppn.Show_At_Resolution_With_Word_In_Figure(c.robotResolution,"jump",1)

cppn.Show_At_Resolution_With_Word_In_Figure(c.robotResolution,"walk",2)

plt.show()
