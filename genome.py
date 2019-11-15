import constants as c

class GENOME:

    def __init__(self,ID):

        self.ID = ID

        # self.cppn = CPPN(ID)

        self.age     = 0

        self.fitness = c.worstFitness

    def Evaluate(self):

        pass

        #robot = np.zeros([resolution,resolution,resolution],dtype='f')

        #self.cppns[cppn].Paint_At_Resolution(robot,resolution)

        #self.cppns[cppn].Compute_Fitness(robot)

    def Get_Age(self):

        return self.age

    def Get_Fitness(self):

        return self.fitness

    def Print(self):

        print(self.ID)
