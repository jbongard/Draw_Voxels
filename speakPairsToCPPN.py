import constants as c
import matplotlib.pyplot as plt
import pickle

cppn = pickle.load( open( "data/cppn.p", "rb" ) )

cppn.Add_W2V_Weights()

fig = plt.figure(1)

panelNum = 1

for word1Index in range(0,c.numWords):

    word1 = c.words[word1Index]

    for word2Index in range(0,c.numWords):

        word2 = c.words[word2Index]

        if word1Index <= word2Index:

            cppn.Show_At_Resolution_With_Words_In_Figure(c.robotResolution,word1,word2,fig,panelNum)

        panelNum = panelNum + 1

plt.show()