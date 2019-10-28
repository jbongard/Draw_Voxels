import copy
import constants as c
import numpy as np
import operator

from cppn import CPPN

class AFPO:

    def __init__(self):

        self.cppns = {}
        self.fitnesses = {}

        for cppn in range(c.popSize):
            self.cppns[cppn] = CPPN()
            self.fitnesses[cppn] = 0.0

    def Evolve_At_Resolution(self,resolution):

        for self.currentGeneration in range(c.numGenerations):
       
            self.Perform_One_Generation(resolution)

    def Show_Best_At_Resolution(self,resolution):

        bestCPPN = self.Find_Best_CPPN()

        self.cppns[bestCPPN].Show_At_Resolution(resolution)

# -------------------------- Private methods ----------------------

    def Age(self):

        for cppn in self.cppns:

            self.cppns[cppn].Age()

    def Aggressor_Dominates_Defender(self,aggressor,defender):

        return self.cppns[aggressor].Dominates(self.cppns[defender])

    def Choose_Aggressor(self):

        return np.random.randint(c.popSize)

    def Choose_Defender(self,aggressor):

        defender = np.random.randint(c.popSize)

        while defender == aggressor:

            defender = np.random.randint(c.popSize)

        return defender

    def Contract(self):

        while len(self.cppns) > c.popSize:

            aggressorDominatesDefender = False

            while not aggressorDominatesDefender:

                aggressor = self.Choose_Aggressor()

                defender  = self.Choose_Defender(aggressor)

                aggressorDominatesDefender = self.Aggressor_Dominates_Defender(aggressor,defender)

            for cppnToMove in range(defender,len(self.cppns)-1):

                self.cppns[cppnToMove] = self.cppns.pop(cppnToMove+1)

    def Evaluate_CPPNs(self,resolution):

        for cppn in self.cppns:

            robot = np.zeros([resolution,resolution,resolution],dtype='f')

            self.cppns[cppn].Paint_At_Resolution(robot,resolution)

            self.cppns[cppn].Compute_Fitness(robot)

    def Expand(self):

        popSize = len(self.cppns)

        for newCPPN in range( popSize , 2 * popSize - 1 ):

            spawner = self.Choose_Aggressor()

            self.cppns[newCPPN] = copy.deepcopy( self.cppns[spawner] )

            self.cppns[newCPPN].Mutate()

    def Inject(self):

        popSize = len(self.cppns)

        self.cppns[popSize-1] = CPPN()

    def Max_Fitness(self):

        maxFitness = -1

        for cppn in self.cppns:

            if self.fitnesses[cppn] > maxFitness:

                maxFitness = self.fitnesses[cppn]

        return maxFitness

    def Perform_One_Generation(self,resolution):

        self.Evaluate_CPPNs(resolution)

        self.Print()

        self.Expand()

        self.Age()

        self.Inject()

        self.Contract()

        self.Print()

    def Print(self):

        print('Generation ', end='')

        print(self.currentGeneration, end='')

        print(' of ', end='')

        print(str(c.numGenerations), end='')

        print('.')

        k = 0

        for cppn in (sorted(self.cppns.values(), key=operator.attrgetter('fitness'),reverse=True)):

            print(k, cppn.Get_Fitness() , cppn.Get_Age())

            k = k + 1

        print()
