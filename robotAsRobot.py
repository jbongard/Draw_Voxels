import constants         as     c
import math
import matplotlib.pyplot as     plt
import numpy             as     np
from   robot             import ROBOT

import sys
sys.path.insert(0, '../pyrosim')
import pyrosim

class ROBOT_AS_ROBOT(ROBOT):

    def Get_Fitness(self):

        return self.Checkerboard()

    def Evaluate_In_Pyrosim(self,playPaused,playBlind,waitToFinish):

        sim = pyrosim.Simulator( play_paused = playPaused , play_blind = playBlind )

        for k in range(0,self.resolution):

            z = self.Z[k]

            for j in range(0,self.resolution):

                y = self.Y[j]

                for i in range(0,self.resolution):

                    x = self.X[i]

                    if self.tensor[k,j,i]:

                        sim.send_box(position=(x,y,z+1.0+c.voxelLength/2.0),sides=(c.voxelLength,c.voxelLength,c.voxelLength))

        sim.start()

        if waitToFinish:

            sim.wait_to_finish()

    def Initialize(self):

        self.resolution = c.robotResolution 

        self.axisMin = -1.0

        self.axisMax = +1.0

        self.X = np.linspace(self.axisMin , self.axisMax , num=self.resolution) 

        self.Y = np.linspace(self.axisMin , self.axisMax , num=self.resolution)     

        self.Z = np.linspace(self.axisMin , self.axisMax , num=self.resolution)

        self.tensor = np.zeros([self.resolution,self.resolution,self.resolution],dtype='f')

    def Paint_With(self,cppn):

        for k in range(0,self.resolution):

            z = self.Z[k]

            for j in range(0,self.resolution): 

                y = self.Y[j]

                for i in range(0,self.resolution):

                    x = self.X[i]

                    inputs = [ z , y , x ]

                    output = cppn.Evaluate_At( inputs ) 

                    if output < 0:

                        self.tensor[k,j,i] = 0 
                    else:
                        self.tensor[k,j,i] = 1

    def Print(self):

        print(self.tensor)

    def Show(self):

        self.Evaluate_In_Pyrosim(playPaused=True,playBlind=False,waitToFinish=False)

        fig = plt.figure()
        ax = fig.gca(projection='3d')
        ax.set_aspect('equal')

        ax.voxels(self.tensor, edgecolor="k")

        plt.show()

# ----------------------- Private methods -----------------------

    def Checkerboard(self):

        leftPart = self.tensor[ : , : , 0:self.resolution-1]

        rightPart = self.tensor[ : , : , 1:self.resolution]

        equalities = leftPart == rightPart

        sumOfEqualities = np.sum( equalities )


        topPart = self.tensor[ : , 0:self.resolution-1 , :]

        bottomPart = self.tensor[ : , 1:self.resolution , :]

        equalities = topPart == bottomPart

        sumOfEqualities = sumOfEqualities + np.sum( equalities )


        frontPart = self.tensor[0:self.resolution-1 , : , : ]

        backPart = self.tensor[ 1:self.resolution , : , : ]

        equalities = frontPart == backPart

        sumOfEqualities = sumOfEqualities + np.sum( equalities )


        return sumOfEqualities
