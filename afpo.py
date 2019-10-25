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
       
    def Compute_Surface_Area_Of(self,robot):

        surfaceArea = 0

        [rows,columns,sheets] = robot.shape

        for row in range(0,rows-1):

            for column in range(0,columns-1):

                for sheet in range(0,sheets-1):

                    if bool( robot[row,column,sheet] ) != bool( robot[row+1,column,sheet] ):

                        surfaceArea = surfaceArea + 1

                    if bool( robot[row,column,sheet] ) != bool( robot[row,column+1,sheet] ):

                        surfaceArea = surfaceArea + 1

                    if bool( robot[row,column,sheet] ) != bool( robot[row,column,sheet+1] ):

                        surfaceArea = surfaceArea + 1

        return surfaceArea

    def Edge_Pieces_Of(self,robot):

        [rows,columns,sheets] = robot.shape

        edgePieces = 0

        [columns,rows,sheets] = robot.shape

        edgePieces = edgePieces + sum(sum(robot[0,:,:]))

        edgePieces = edgePieces + sum(sum(robot[rows-1,:,:]))

        edgePieces = edgePieces + sum(sum(robot[:,0,:]))

        edgePieces = edgePieces + sum(sum(robot[:,columns-1,:]))

        edgePieces = edgePieces + sum(sum(robot[:,:,0]))

        edgePieces = edgePieces + sum(sum(robot[:,:,sheets-1]))

        return edgePieces 

    def Evaluate_CPPNs(self,resolution):

        for cppn in self.cppns:

            robot = np.zeros([resolution,resolution,resolution],dtype='f')

            numComponents = self.cppns[cppn].Paint_At_Resolution(robot,resolution)

            surfaceArea = self.Compute_Surface_Area_Of(robot)

            penaltyForEdgePieces = -1 * self.Edge_Pieces_Of(robot)

            self.fitnesses[cppn] = penaltyForEdgePieces + surfaceArea

            if numComponents != 1:

                self.fitnesses[cppn] = -1000000000

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

        self.Compete_CPPNs()

    def Print(self):

        print('Generation ', end='')

        print(self.currentGeneration, end='')

        print(' of ', end='')

        print(str(c.numGenerations), end='')

        print(': ', end='')

        print(str(self.Max_Fitness()) + '   ', end='')

        for cppn in self.cppns:

            print( str(self.fitnesses[cppn]) + ' ' , end='')

        print()
