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

    def Evolve(self):

        for self.currentGeneration in range(c.numGenerations):
       
            self.Perform_One_Generation()

    def Show_Best(self):

        self.cppns[0].Show()

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
        
    def Evaluate_CPPNs(self):

        for cppn in self.cppns:

            robot = np.zeros([c.robotResolution,c.robotResolution,c.robotResolution],dtype='f')

            numComponents = self.cppns[cppn].Paint(robot)

            self.fitnesses[cppn] = numComponents

    def Max_Fitness(self):

        maxFitness = -1

        for cppn in self.cppns:

            if self.fitnesses[cppn] > maxFitness:

                maxFitness = self.fitnesses[cppn]

        return maxFitness

    def Perform_One_Generation(self):

        self.Evaluate_CPPNs()

        self.Print()

        self.Compete_CPPNs()

    def Print(self):

        print(self.currentGeneration,self.Max_Fitness())
