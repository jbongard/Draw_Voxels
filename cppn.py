import matplotlib.pyplot as plt
from   mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import constants as c
import math
import numpy as np
import pickle
from   scipy.ndimage import label

import sys
sys.path.insert(0, "/Users/jbongard/Dropbox/JoshBongard/0_Code/TPR_3")
from database.word2vecDatabase import Word2VecVectorSpace

class CPPN: 

    def __init__(self,ID):

        self.Set_ID(ID)

        self.fitness      = c.worstFitness

        self.age          = 0

        self.inputLayer   = np.zeros(c.cppnInputs,dtype='f')

        self.IHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnInputs,c.cppnHiddens] )

        self.hiddenLayer1 = np.zeros(c.cppnHiddens,dtype='f')

        self.activeLayer1 = {}

        for h in range(c.cppnHiddens):

            activationFunctionType = np.random.randint(c.numCPPNActivationFunctions)

            self.activeLayer1[h] = c.cppnActivationFunctions[activationFunctionType] 

        self.HHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,c.cppnHiddens] )

        self.hiddenLayer2 = np.zeros(c.cppnHiddens,dtype='f')

        self.activeLayer2 = {}

        for h in range(c.cppnHiddens):

            activationFunctionType = np.random.randint(c.numCPPNActivationFunctions)

            self.activeLayer2[h] = c.cppnActivationFunctions[activationFunctionType]

        self.HOWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,c.cppnOutputs] )

        self.outputLayer  = np.zeros(c.cppnOutputs,dtype='f')

    def Add_W2V_Weights(self):

        self.word2vecVectorSpace = Word2VecVectorSpace(database_file='/Users/jbongard/Dropbox/JoshBongard/0_Code/TPR_3/database/w2vVectorSpace-google.db')

        word = "jump"

        vec = self.word2vecVectorSpace.get_vector( word )

        self.w2vLength = len(vec)

        self.v1HWeights = np.random.uniform( c.cppnInitialMinW2VWeight , c.cppnInitialMaxW2VWeight , [self.w2vLength,c.cppnHiddens] )

        self.v2HWeights = np.random.uniform( c.cppnInitialMinW2VWeight , c.cppnInitialMaxW2VWeight , [self.w2vLength,c.cppnHiddens] )

    def Age(self):

        self.age = self.age + 1

    def Compute_Fitness(self,robot):

        surfaceArea = self.Compute_Surface_Area_Of(robot)

        symmetryScore = self.Compute_Symmetry(robot)

        numEdgePieces = self.Edge_Pieces_Of(robot)

        labelledRobot , numComponents = self.Extract_Largest_Component(robot)

        if numComponents != 1:

            self.fitness = c.worstFitness 
        else:
            self.fitness = symmetryScore * surfaceArea * ( 1 / (1 + numEdgePieces) ) # penaltyForEdgePieces + surfaceArea

    def Dominates(self,other):

        if self.Get_Fitness() >= other.Get_Fitness():

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

    def Get_ID(self):

        return self.ID

    def Mutate(self):

        if np.random.randint(2) == 0:

            self.Mutate_A_Weight()
        else:
            self.Mutate_An_Activation_Function()

    def Paint_At_Resolution(self,robot,resolution):

        self.Paint_At_Resolution_With_Words(robot,resolution,"","")

    def Paint_At_Resolution_With_Word(self,robot,resolution,word):

        self.Paint_At_Resolution_With_Words(self,robot,resolution,word,"")

    def Paint_At_Resolution_With_Words(self,robot,resolution,word1,word2):

        cols,rows,sheets = robot.shape

        for x in range(cols):
            xScaled = self.Scale_Using_Resolution(x,resolution)
            for y in range(rows):
                yScaled = self.Scale_Using_Resolution(y,resolution)
                for z in range(sheets):
                    zScaled = self.Scale_Using_Resolution(z,resolution)
                    vals = self.Evaluate_At_With_Words(xScaled,yScaled,zScaled,word1,word2)

                    if vals[0] > 0:
                        robot[x,y,z] = 1
                    else:
                        robot[x,y,z] = 0

                    if vals[1] > 0 and robot[x,y,z]==1:

                        robot[x,y,z] = 2

    def Print(self):

        print(self.fitness,self.age)

    def Set_ID(self,ID):

        self.ID = ID

    def Save(self,randomSeed):

        pickle.dump( self , open( "data/cppn"+str(randomSeed)+".p", "wb" ) )

        
    def Show_At_Resolution(self,resolution,fig):

        self.Show_At_Resolution_With_Words_In_Figure(resolution,"","",fig,1)

    def Show_At_Resolution_With_Word_In_Figure(self,resolution,word,fig,panelNumber):

        self.Show_At_Resolution_With_Word_In_Figure(resolution,word,"",fig,panelNumber)
        
    def Show_At_Resolution_With_Words_In_Figure(self,resolution,word1,word2,fig,panelNumber):

        robot = np.zeros([resolution,resolution,resolution],dtype='f')

        self.Paint_At_Resolution_With_Words(robot,resolution,word1,word2)

        facecolors = np.where(robot==2, 'salmon', 'lightgreen')

        ax = fig.add_subplot(c.numWords, c.numWords, panelNumber, projection='3d')

        if panelNumber <= c.numWords:

            ax.set_title('"' + word2 + '"')

        if panelNumber % c.numWords == 1 :

            ax.set_zlabel('Z axis')

        ax.voxels(robot, facecolors=facecolors , edgecolors = 'k')

        ax.set_aspect('equal')

        ax.set_axis_off()

# ---------------- Private methods -----------

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

    def Compute_Symmetry(self,robot):

        leftHalf  = robot[ : , 0 : int( c.robotResolution / 2 ) , : ]

        rightHalf = robot[ : , int(c.robotResolution/2) :       , : ] 

        flippedRightHalf = np.flip( rightHalf , axis = 1 )

        matchingVoxels = leftHalf == flippedRightHalf

        numMatchingVoxels = sum(sum(sum(matchingVoxels)))

        return numMatchingVoxels

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

    def Extract_Largest_Component(self,robot):

        labelledRobot, num_labels = label(robot,structure=[[[0,0,0],[0,1,0],[0,0,0]],[[0,1,0],[1,1,1],[0,1,0]],[[0,0,0],[0,1,0],[0,0,0]]])

        return labelledRobot, np.amax(labelledRobot)

    def Get_Action_From_Outputs(self,outputs):

        possibleActions = outputs[ 0 : c.numEdgeChangeActions ]

        action = np.argmax( possibleActions )

        return action 

    def Get_Age(self):

        return self.age

    def Get_DeltaX_From_Outputs(self,outputs):

        # return outputs[c.numEdgeChangeActions]

        minusOneToOne = outputs[c.numEdgeChangeActions]

        minusDeltaXToDeltaX = minusOneToOne * c.vectorFieldXDeltaMax

        return minusDeltaXToDeltaX 

    def Get_DeltaY_From_Outputs(self,outputs):

        # return outputs[c.numEdgeChangeActions+1]

        minusOneToOne = outputs[c.numEdgeChangeActions+1]

        minusDeltaYToDeltaY = minusOneToOne * c.vectorFieldYDeltaMax

        return minusDeltaYToDeltaY

    def Get_Fitness(self):

        return self.fitness

    def Evaluate_At_With_Word(self,x,y,z,word):

        self.Evaluate_At_With_Words(x,y,z,word,"")

    def Evaluate_At_With_Words(self,x,y,z,word1,word2):

        self.inputLayer[0] = x

        self.inputLayer[1] = y

        self.inputLayer[2] = z

        self.inputLayer[3] = math.sqrt( x**2 + y**2 + z**2 )

        self.inputLayer[4] = 1 # Bias

        self.hiddenLayer1 = np.dot( self.inputLayer   , self.IHWeights )

        if word1 != "":

            vec = self.word2vecVectorSpace.get_vector( word1 )

            self.hiddenLayer1 = self.hiddenLayer1 + np.dot( vec   , self.v1HWeights )

        if word2 != "":

            vec = self.word2vecVectorSpace.get_vector( word2 )

            self.hiddenLayer1 = self.hiddenLayer1 + np.dot( vec   , self.v2HWeights )

        for h in range(c.cppnHiddens):

            self.hiddenLayer1[h] = self.activeLayer1[h]( self.hiddenLayer1[h] )


        self.hiddenLayer2 = np.dot( self.hiddenLayer1 , self.HHWeights )

        for h in range(c.cppnHiddens):

            self.hiddenLayer2[h] = self.activeLayer2[h]( self.hiddenLayer2[h] )


        self.outputLayer  = np.tanh( np.dot( self.hiddenLayer2 , self.HOWeights ) )


        return self.outputLayer 

    def Gaussian(self,x):

        return np.exp( -x**2 / 2.0 )

    def Is_Newer_Than(self,other):

        return self.Get_ID() > other.Get_ID()

    def Mutate_A_Weight(self):

        mutateLayer = np.random.randint(3)

        if mutateLayer == 0:

            self.Mutate_A_Weight_In(self.IHWeights)

        elif mutateLayer == 1:

            self.Mutate_A_Weight_In(self.HHWeights)

        else:
            self.Mutate_A_Weight_In(self.HOWeights)

    def Mutate_A_Weight_In(self,W):

        cols, rows = W.shape

        col = np.random.randint(cols)
        row = np.random.randint(rows)

        W[col,row] = np.random.normal( loc = W[col,row] , scale = np.abs(W[col,row]) )

    def Mutate_An_Activation_Function(self):

        mutateLayer = np.random.randint(2)

        if mutateLayer == 0:

            self.Mutate_An_Activation_Function_In(self.activeLayer1)

        elif mutateLayer == 1:

            self.Mutate_An_Activation_Function_In(self.activeLayer2)

    def Mutate_An_Activation_Function_In(self,activeLayer):

        h = np.random.randint(c.cppnHiddens)

        activationFunctionType = np.random.randint(c.numCPPNActivationFunctions)

        activeLayer[h] = c.cppnActivationFunctions[activationFunctionType]

    def Scale_Using_Resolution(self,OldValue,resolution):

        OldMin = 0
        OldMax = resolution - 1

        NewMin = -1.0
        NewMax = +1.0

        OldRange = (OldMax - OldMin)  
        NewRange = (NewMax - NewMin)  
        NewValue = (((OldValue - OldMin) * NewRange) / OldRange) + NewMin

        return NewValue
