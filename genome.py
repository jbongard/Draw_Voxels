import constants     as     c
from   cppn          import CPPN
from   robotAsMatrix import ROBOT_AS_MATRIX

class GENOME:

    def __init__(self,ID):

        self.ID = ID

        self.cppn = CPPN(inputWidth=2,outputWidth=1)

        self.cppn.Print()

        self.age     = 0

        self.fitness = c.worstFitness

    def Evaluate(self):

        robot = ROBOT_AS_MATRIX()

        self.cppn.Paint(robot)

        # self.Compute_Fitness(robot)

    def Get_Age(self):

        return self.age

    def Get_Fitness(self):

        return self.fitness

    def Print(self):

        print(self.ID)

# ---------------------------- Private methods ---------------------------

    def Compute_Fitness(self,robot):

        self.fitness = c.worstFitness
    
