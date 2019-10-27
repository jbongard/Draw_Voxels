import copy
import constants as c
import numpy as np

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

    def Aggressor_Beats_Defender(self,aggressor,defender):

        return self.fitnesses[aggressor] >= self.fitnesses[defender]

    def Compete_CPPNs(self):

        aggressor = np.random.randint(c.popSize)

        defender = np.random.randint(c.popSize)

        while defender == aggressor:

            defender = np.random.randint(c.popSize)

        if self.Aggressor_Beats_Defender(aggressor,defender):

            newCPPN = copy.deepcopy( self.cppns[aggressor] )

            newCPPN.Mutate()

            self.cppns[defender] = newCPPN
       
    def Evaluate_CPPNs(self,resolution):

        for cppn in self.cppns:

            robot = np.zeros([resolution,resolution,resolution],dtype='f')

            self.cppns[cppn].Paint_At_Resolution(robot,resolution)

            self.cppns[cppn].Compute_Fitness(robot)

    def Find_Best_CPPN(self):

        maxFitness = -1000000000
        bestCPPN   = -1

        for cppn in self.cppns:

            if self.fitnesses[cppn] > maxFitness:

                maxFitness = self.fitnesses[cppn]
                bestCPPN   = cppn

        return bestCPPN 

    def Max_Fitness(self):

        maxFitness = -1

        for cppn in self.cppns:

            if self.fitnesses[cppn] > maxFitness:

                maxFitness = self.fitnesses[cppn]

        return maxFitness

    def Perform_One_Generation(self,resolution):

        self.Evaluate_CPPNs(resolution)

        self.Print()

        exit()

        #self.Compete_CPPNs()

    def Print(self):

        print('Generation ', end='')

        print(self.currentGeneration, end='')

        print(' of ', end='')

        print(str(c.numGenerations), end='')

        print(': ', end='')

        for cppn in self.cppns:

            self.cppns[cppn].Print()

        print()
