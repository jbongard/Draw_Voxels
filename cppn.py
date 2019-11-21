import matplotlib.pyplot as plt
from   mpl_toolkits.mplot3d import Axes3D  # noqa: F401 unused import
import constants as c
import itertools
import math
import numpy as np
import pickle
from   scipy.ndimage import label
from   scipy import signal
from   scipy.stats import rankdata

import sys
sys.path.insert(0, "/Users/jbongard/Dropbox/JoshBongard/0_Code/TPR_3")
from database.word2vecDatabase import Word2VecVectorSpace

class CPPN: 

    def __init__(self,inputWidth,outputWidth):

        self.inputWidth   = inputWidth + 1 # Add a bias neuron

        self.outputWidth  = outputWidth

        self.Create_Input_Layer()

        self.Create_First_Hidden_Layer()

        self.Create_Second_Hidden_Layer()

        self.Create_Output_Layer()

    def Evaluate_At(self,inputs):

        self.inputLayer[0:len(inputs)] = inputs

        self.Evaluate_Hidden_Layer_One()

        self.Evaluate_Hidden_Layer_Two()

        self.Evaluate_Output_Layer()

        return self.outputLayer

    def Print(self):

        print(self.inputLayer)

        print(self.hiddenLayer1)

        print(self.hiddenLayer2)

        print(self.outputLayer)

        print('')


# -------------- Private methods --------------------

    def Apply_Activation_Functions_To_Hidden_Layer_One(self):

        for h in range(c.cppnHiddens):

            self.hiddenLayer1[h] = self.activeLayer1[h]( self.hiddenLayer1[h] )

    def Apply_Activation_Functions_To_Hidden_Layer_Two(self):

        for h in range(c.cppnHiddens):

            self.hiddenLayer2[h] = self.activeLayer2[h]( self.hiddenLayer2[h] )

    def Create_First_Hidden_Layer(self):

        self.Create_IH_Weights()

        self.hiddenLayer1 = np.zeros(c.cppnHiddens,dtype='f')

        self.activeLayer1 = {}

        for h in range(c.cppnHiddens):

            activationFunctionType = np.random.randint(c.numCPPNActivationFunctions)

            self.activeLayer1[h] = c.cppnActivationFunctions[activationFunctionType]

    def Create_HH_Weights(self):

        self.HHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,c.cppnHiddens] )

    def Create_HO_Weights(self):

        self.HOWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [c.cppnHiddens,self.outputWidth] )

    def Create_Input_Layer(self):

        self.inputLayer   = np.zeros(self.inputWidth,dtype='f')

        self.inputLayer[self.inputWidth-1] = 1 # The bias neuron.

    def Create_IH_Weights(self):

        self.IHWeights    = np.random.uniform( c.cppnInitialMinWeight , c.cppnInitialMaxWeight , [self.inputWidth,c.cppnHiddens] )

    def Create_Output_Layer(self):

        self.Create_HO_Weights()

        self.outputLayer  = np.zeros(self.outputWidth,dtype='f')

    def Create_Second_Hidden_Layer(self):

        self.Create_HH_Weights()

        self.hiddenLayer2 = np.zeros(c.cppnHiddens,dtype='f')

        self.activeLayer2 = {}

        for h in range(c.cppnHiddens):

            activationFunctionType = np.random.randint(c.numCPPNActivationFunctions)

            self.activeLayer2[h] = c.cppnActivationFunctions[activationFunctionType]

    def Evaluate_Hidden_Layer_One(self):

        self.hiddenLayer1 = np.dot( self.inputLayer   , self.IHWeights )

        self.Apply_Activation_Functions_To_Hidden_Layer_One()

    def Evaluate_Hidden_Layer_Two(self):

        self.hiddenLayer2 = np.dot( self.hiddenLayer1 , self.HHWeights )

        self.Apply_Activation_Functions_To_Hidden_Layer_Two()

    def Evaluate_Output_Layer(self):

        self.outputLayer  = np.tanh( np.dot( self.hiddenLayer2 , self.HOWeights ) )

    def Mutate(self):

        if np.random.randint(2) == 0:

            self.Mutate_A_Weight()
        else:
            self.Mutate_An_Activation_Function()

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

    def Save(self,randomSeed):

        pickle.dump( self , open( "data/cppn"+str(randomSeed)+".p", "wb" ) )

