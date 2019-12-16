import constants     as     c

import sys
sys.path.insert(0, "..")

from   CPPNs.cppn    import CPPN

from   robotAsRobot import ROBOT_AS_ROBOT

class GENOME:

    def __init__(self,ID):

        self.Set_ID(ID)

        self.cppn = CPPN(inputWidth=2,outputWidth=4)

        self.age     = 0

        self.fitness = c.worstFitness

    def Age(self):

        self.age = self.age + 1

    def Dominates(self,other):

        if self.Get_Fitness() <= other.Get_Fitness():

            if self.Get_Age() <= other.Get_Age():

                equalFitnesses = self.Get_Fitness() == other.Get_Fitness()

                equalAges      = self.Get_Age()     == other.Get_Age()

                if not equalFitnesses and equalAges:

                    return True
                else:
                    return self.Is_Newer_Than(other)
            else:
                return False
        else:
            return False

    def Evaluate(self):

        robot = ROBOT_AS_ROBOT()

        robot.Paint_With(self.cppn)

        # robot.Evaluate_In_Pyrosim( playPaused = False , playBlind = True , waitToFinish = True)

        self.fitness = robot.Get_Fitness()

    def Get_Age(self):

        return self.age

    def Get_Fitness(self):

        return self.fitness

    def Mutate(self):

        self.cppn.Mutate()

    def Print(self):

        print(' fitness: ' , end = '' )
        print(self.fitness , end = '' )

        print(' age: '     , end = '' )
        print(self.age     , end = '' )

        print()

    def Save(self,randomSeed):

        self.cppn.Save(randomSeed)

    def Set_ID(self,ID):

        self.ID = ID

    def Show(self):

        robot = ROBOT_AS_ROBOT()

        robot.Paint_With(self.cppn)

        robot.Show()

# -------------------- Private methods ----------------------

    def Get_ID(self):

        return self.ID

    def Is_Newer_Than(self,other):

        return self.Get_ID() > other.Get_ID()
