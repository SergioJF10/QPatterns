'''Module including all the elements needed for adapting the Flyweight pattern'''
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
        print(f'[ConcreteFlyweight] Quantum Operation Result: {MeasureSuperposition.simulate()}')

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


class Client():
    '''Client class calling the operations'''
    def __init__(self, factory):
        self.factory = factory

    def Main(self):
        '''Method for simulating the use of the factory'''
        fly1 = factory.GetFlyweight('A')
        print('[Client] Calling ConcreteFlyweight A')
        fly1.Operation()

        fly2 = factory.GetFlyweight('B')
        print('[Client] Calling ConcreteFlyweight B')
        fly2.Operation()

        fly3 = factory.GetFlyweight('C')
        print('[Client] Calling ConcreteFlyweight C')
        fly3.Operation()

# MAIN
factory = FlyweightFactory()
client = Client(factory)
client.Main()