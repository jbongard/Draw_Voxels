import matplotlib.pyplot as     plt
import numpy             as     np
from   robot             import ROBOT

class ROBOT_AS_MATRIX(ROBOT):

    def Get_Fitness(self):

        return np.sum( self.matrix )

    def Initialize(self):

        self.X = np.linspace(-1.0,+1.0, num=2) 

        self.Y = np.linspace(-1.0,+1.0, num=2)     

        self.matrix = np.zeros([2,2],dtype='f')

    def Paint_With(self,cppn):

        for j in range(0,2):

            y = self.Y[j]

            for i in range(0,2):

                x = self.X[i]

                inputs = [ y , x ]

                self.matrix[j,i] = cppn.Evaluate_At( inputs ) 

    def Print(self):

        print(self.matrix)

    def Show(self):

        fig = plt.figure(1)

        plt.show()

