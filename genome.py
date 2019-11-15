import constants as c

class GENOME:

    def __init__(self,ID):

        self.ID = ID

        # self.cppn = CPPN(ID)

        self.fitness = c.worstFitness

    def Evaluate(self):

        self.Print()

        #robot = np.zeros([resolution,resolution,resolution],dtype='f')

        #self.cppns[cppn].Paint_At_Resolution(robot,resolution)

        #self.cppns[cppn].Compute_Fitness(robot)

    def Print(self):

        print(self.ID)
