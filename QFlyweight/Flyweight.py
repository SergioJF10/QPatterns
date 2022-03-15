from abc import ABC, abstractmethod
import qsharp
from Superposition import MeasureSuperposition

# print(qsharp.get_available_operations_by_namespace())

class Flyweight(ABC):
    '''Abstract class for the flyweights'''
    
    @abstractmethod
    def Operation(self):
        pass

class ConcreteFlyweight(Flyweight):
    '''Implementation of the Flyweight class'''
    
    def __init__(self):
        self.allState = ''
    
    def Operation(self):
        '''Inherited method implementing the Quantum operation'''
        print(MeasureSuperposition.simulate())

class FlyweightFactory():
    '''FlyweightFactory class for managing the existance of several Flyweights'''
    def __init__(self):
        self.flyweights = dict()

    def GetFlyweight(self, key):
        '''Method providing the corresponding Flyweight instance'''
        flyweight = None
        try:
            flyweight = self.flyweights[key]
        except KeyError:
            self.flyweights[key] = ConcreteFlyweight()
            flyweight = self.flyweights[key]

        return flyweight


# MAIN
factory = FlyweightFactory()

fly1 = factory.GetFlyweight('A')
fly1.Operation()

fly2 = factory.GetFlyweight('B')
fly2.Operation()

fly3 = factory.GetFlyweight('C')
fly3.Operation()