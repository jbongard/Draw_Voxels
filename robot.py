from abc import ABC, abstractmethod
 
class ROBOT(ABC):
 
    def __init__(self):

        self.Initialize()
    
    @abstractmethod
    def Initialize(self):
        pass

    @abstractmethod
    def Show(self):
        pass
