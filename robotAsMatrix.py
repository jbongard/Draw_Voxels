import constants         as     c
import matplotlib.pyplot as     plt
import numpy             as     np
from   robot             import ROBOT

class ROBOT_AS_MATRIX(ROBOT):

    def Get_Fitness(self):

        return np.sum( self.matrix )

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

                self.matrix[j,i] = cppn.Evaluate_At( inputs ) 

    def Print(self):

        print(self.matrix)

    def Show(self):

        plt.matshow( self.matrix , cmap='gray' )

        plt.xticks( [ 0 , self.resolution-1 ] , labels = [ self.axisMin , self.axisMax ] )

        plt.yticks( [ 0 , self.resolution-1 ] , labels = [ self.axisMin , self.axisMax ] )

        plt.show()

