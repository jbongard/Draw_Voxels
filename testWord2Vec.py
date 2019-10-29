import sys

sys.path.insert(0, "/Users/jbongard/Dropbox/JoshBongard/0_Code/TPR_3")

from database.word2vecDatabase import Word2VecVectorSpace

word2vecVectorSpace = Word2VecVectorSpace(database_file='/Users/jbongard/Dropbox/JoshBongard/0_Code/TPR_3/database/w2vVectorSpace-google.db')

word = "jump"
vec = word2vecVectorSpace.get_vector( word )
print(len(vec),vec)

word = "twist"
vec = word2vecVectorSpace.get_vector( word )
print(vec)

