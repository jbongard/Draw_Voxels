import constants         as     c
import math
import matplotlib.pyplot as     plt
import numpy             as     np
from   robot             import ROBOT

class ROBOT_AS_MATRIX(ROBOT):

    def Get_Fitness(self):

        # return self.Number_Of_Ones()

        # return self.Number_Of_Zeros()

        # return self.Half_Ones()

        return self.Checkerboard()

    def Initialize(self):

        self.resolution = 10

        self.axisMin = -1.0

        self.axisMax = +1.0

        self.X = np.linspace(self.axisMin , self.axisMax , num=self.resolution) 

        self.Y = np.linspace(self.axisMin , self.axisMax , num=self.resolution)     

        self.matrix = np.zeros([self.resolution,self.resolution],dtype='f')

    def Paint_With(self,cppn):

        for j in range(0,self.resolution): 

            y = self.Y[j]

            for i in range(0,self.resolution):

                x = self.X[i]

                inputs = [ y , x ]

                output = cppn.Evaluate_At( inputs ) 

                if output < 0:

                   self.matrix[j,i] = 0 
                else:
                   self.matrix[j,i] = 1

    def Print(self):

        print(self.matrix)

    def Show(self):

        plt.matshow( self.matrix , cmap='gray' , vmin = 0 , vmax = 1 )

        plt.xticks( [ 0 , self.resolution-1 ] , labels = [ self.axisMin , self.axisMax ] )

        plt.yticks( [ 0 , self.resolution-1 ] , labels = [ self.axisMin , self.axisMax ] )

        plt.show()

# ----------------------- Private methods -----------------------

    def Checkerboard(self):

        leftPart = self.matrix[ : , 0:self.resolution-1]

        rightPart = self.matrix[ : , 1:self.resolution]

        differences = np.fabs( leftPart - rightPart )

        sumOfDifferences = np.sum( differences )

        topPart = self.matrix[0:self.resolution-1 , :]

        bottomPart = self.matrix[ 1:self.resolution , :]

        differences = np.fabs( topPart - bottomPart )

        sumOfDifferences = sumOfDifferences + np.sum( differences )

        return -sumOfDifferences # As many differences as possible

    def Half_Ones(self):

        numberOfOnes = np.sum( self.matrix )

        numberOfElements = self.resolution * self.resolution

        proximityToHalfOnes = math.fabs( numberOfElements/2.0 - numberOfOnes )

        return proximityToHalfOnes

    def Number_Of_Ones(self):

        numberOfOnes = np.sum( self.matrix )

        return numberOfOnes

    def Number_Of_Zeros(self):

        numberOfElements = self.resolution * self.resolution

        numberOfZeros    = numberOfElements - np.sum( self.matrix )

        return numberOfZeros

