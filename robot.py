from abc import ABC, abstractmethod
 
class ROBOT(ABC):
 
    def __init__(self):

        self.Initialize()

    @abstractmethod
    def Get_Fitness(self):
        pass
    
    @abstractmethod
    def Initialize(self):
        pass

    @abstractmethod
    def Paint_With(self,cppn):
        pass

    @abstractmethod
    def Show(self):
        pass
