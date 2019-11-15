import constants     as     c
from   cppn          import CPPN
from   robotAsMatrix import ROBOT_AS_MATRIX

class GENOME:

    def __init__(self,ID):

        self.ID = ID

        self.cppn = CPPN(inputWidth=2,outputWidth=1)

        self.age     = 0

        self.fitness = c.worstFitness

    def Evaluate(self):

        robot = ROBOT_AS_MATRIX()

        robot.Paint_With(self.cppn)

        self.fitness = robot.Get_Fitness()

    def Get_Age(self):

        return self.age

    def Get_Fitness(self):

        return self.fitness

    def Print(self):

        print(self.fitness , self.age)

    def Show(self):

        robot = ROBOT_AS_MATRIX()

        robot.Paint_With(self.cppn)

        robot.Show()
