'''Module including the necessary classes for implementing the Decorator Pattern in a sample hybrid small system'''

import qsharp
from abc import ABC, abstractmethod
from QuantumComponents import OpX, OpY, OpZ

class Component(ABC):
    '''Component abstract class, father for the Decorators and ConcreteComponents'''
    @abstractmethod
    def Operation(self):
        pass

class ConcreteComponent(Component):
    '''Concrete implementation of the Component class defining an interface for increasing the Decorators functionalities (the Z gate Quantum Algorithm)'''

    def Operation(self):
        '''Operation of the component calling the Quantum Algorithm'''
        print(f'Concrete Component operation result [Z-GATE]: {OpZ.simulate()}')

class Decorator(Component, ABC):
    '''Decorator abstract class Component's child that extends its functionality'''
    @abstractmethod
    def __init__(self):
        self.component = None

    @abstractmethod
    def SetComponent(self, component):
        '''Abstract method for adding more components to the decorator'''
        self.component = component

    @abstractmethod
    def Operation(self):
        '''Decorator abstract self operation'''
        if self.component is not None:
            self.component.Operation()

class ConcreteDecoratorY(Decorator):
    '''Concrete class inheriting from the Decorator class implementing the functinality of calling the Quantum Y gate algorithm'''
    def __init__(self):
        super().__init__()

    def SetComponent(self, component):
        '''Implementation of the abstract method from the Decorator class for setting a new component'''
        return super().SetComponent(component)

    def Operation(self):
        '''Operation calling the Quantum Algorithm for the Pauli Y gate'''
        super().Operation()
        print(f'Concrete Decorator Y operation result [Y-GATE]: {OpY.simulate()}') # Added operation

class ConcreteDecoratorX(Decorator):
    '''Concrete class inheriting from the Decorator class implementing the functionality of calling the Quantum X gate algorithm'''
    def __init__(self):
        super().__init__()

    def SetComponent(self, component):
        '''Implementation of the abstract method from the Decorator class for settintg a new component'''
        return super().SetComponent(component)

    def Operation(self):
        '''Operation calling the Quantum Algorithm for the Pauli X gate'''
        print('TOTAL DECORATOR X OPERATION...')
        super().Operation()
        print(f'Concrete Decorator X operation result [X-GATE]: {OpX.simulate()}') # Added operation

class Client:
    '''Client class for calling the operations from the Decorator Pattern'''
    def __init__(self):
        self.concrete_component = ConcreteComponent()
        self.concrete_deco_Y = ConcreteDecoratorY()
        self.concrete_deco_X = ConcreteDecoratorX()

    def Main(self):
        '''Main method'''
        self.concrete_deco_Y.SetComponent(self.concrete_component)
        self.concrete_deco_X.SetComponent(self.concrete_deco_Y)

        self.concrete_deco_X.Operation()

# MAIN
Client().Main()