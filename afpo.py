import constants as c
import copy
import numpy     as np
import operator

from genome import GENOME 

class AFPO:

    def __init__(self,randomSeed):

        self.randomSeed = randomSeed

        self.currentGeneration = 0

        self.nextAvailableID = 0

        self.genomes = {}

        for populationPosition in range(c.popSize):

            self.genomes[populationPosition] = GENOME(self.nextAvailableID)

            self.nextAvailableID = self.nextAvailableID + 1

    def Evolve(self):

        self.Perform_First_Generation()

        for self.currentGeneration in range(1,c.numGenerations):
       
             self.Perform_One_Generation()

        self.Show_Best_Genome()

# -------------------------- Private methods ----------------------

    def Age(self):

        for genome in self.genomes:

            self.genomes[genome].Age()

    def Aggressor_Dominates_Defender(self,aggressor,defender):

        return self.genomes[aggressor].Dominates(self.genomes[defender])

    def Choose_Aggressor(self):

        return np.random.randint(c.popSize)

    def Choose_Defender(self,aggressor):

        defender = np.random.randint(c.popSize)

        while defender == aggressor:

            defender = np.random.randint(c.popSize)

        return defender

    def Contract(self):

        while len(self.genomes) > c.popSize:

            aggressorDominatesDefender = False

            while not aggressorDominatesDefender:

                aggressor = self.Choose_Aggressor()

                defender  = self.Choose_Defender(aggressor)

                aggressorDominatesDefender = self.Aggressor_Dominates_Defender(aggressor,defender)

            for genomeToMove in range(defender,len(self.genomes)-1):

                self.genomes[genomeToMove] = self.genomes.pop(genomeToMove+1)

    def Evaluate_Genomes(self):

        for genome in self.genomes:

            self.genomes[genome].Evaluate()

    def Expand(self):

        popSize = len(self.genomes)

        for newGenome in range( popSize , 2 * popSize - 1 ):

            spawner = self.Choose_Aggressor()

            self.genomes[newGenome] = copy.deepcopy( self.genomes[spawner] )

            self.genomes[newGenome].Set_ID(self.nextAvailableID)

            self.nextAvailableID = self.nextAvailableID + 1

            self.genomes[newGenome].Mutate()

    def Find_Best_Genome(self):

        genomesSortedByFitness = sorted(self.genomes.values(), key=operator.attrgetter('fitness'),reverse=False)

        return genomesSortedByFitness[0]

    def Inject(self):

        popSize = len(self.genomes)

        self.genomes[popSize-1] = GENOME(self.nextAvailableID)

        self.nextAvailableID = self.nextAvailableID + 1

    def Perform_First_Generation(self):

        self.Evaluate_Genomes()

        self.Print()

        self.Save_Best()

    def Perform_One_Generation(self):

        self.Expand()

        self.Age()

        self.Inject()

        self.Evaluate_Genomes()

        self.Contract()

        self.Print()

        self.Save_Best()

    def Print(self):

        print('Generation ', end='')

        print(self.currentGeneration, end='')

        print(' of ', end='')

        print(str(c.numGenerations), end='')

        print(': ', end='')

        bestGenome = self.Find_Best_Genome()
 
        bestGenome.Print()

    def Save_Best(self):

        bestGenome = self.Find_Best_Genome()

        bestGenome.Save(self.randomSeed)

    def Show_Best_Genome(self):

        bestGenome = self.Find_Best_Genome()

        bestGenome.Show()
