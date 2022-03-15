'''Module with all the elements needed for implementing a dummy sample hybrid information system applying the Composite Pattern'''

import qsharp
from QuantumGates import OpX, OpY
from abc import ABC, abstractmethod

class Component(ABC):
    '''Abstract class representing the interface for the Composite Pattern Tree Structure'''
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def Operation(self):
        '''Abstract method for the operation of a Component child'''
        pass

    @abstractmethod
    def Add(self, component):
        '''Abstract method for adding a component to the tree'''
        pass

    @abstractmethod
    def Remove(self, component):
        '''Abstract method for removing a component from the tree'''
        pass

    @abstractmethod
    def Operation(self):
        '''Abstract method for doing the operation of the component'''
        pass

class Composite(Component):
    '''Implementation of the Component Abstract class representing a non-terminal node from the pattern tree'''
    def __init__(self, name):
        super().__init__(name)
        self.children = list()
    
    def Add(self, component):
        '''Implementation of the Add method for adding a new component to this Composite node'''
        self.children.append(component)

    def Remove(self, component):
        '''Implementation of the Remove method for removing a component to this Composite node'''
        self.children.remove(component)

    def Operation(self):
        '''Implementation of the Operation method for executing the operation of the composite and its children'''
        print(f'[Composite {self.name}] Pauli Y Result: {OpY.simulate()}')

        for child in self.children:
            print('\t', end="")
            child.Operation()

class Leaf(Component):
    '''Implementation of the Component Abstract class representing a terminal node from the pattern tree'''
    def __init__(self, name):
        super().__init__(name)

    def Add(self, component):
        '''Since a leaf cannot add more components, just prints an error'''
        print(f'The node {self.name} is a leaf, you cannot add a component to it')

    def Remove(self, component):
        '''Since a leaf cannot remove any components, just prints an error'''
        print(f'The node {self.name} is a leaf, you cannot remove any component from it')

    def Operation(self):
        '''Implementation of the Operation method for executing the operation of the composite and its children'''
        print(f'[Leaf {self.name}] Pauli X Result: {OpX.simulate()}')

# MAIN
root = Composite('Root')
root.Add(Leaf('Leaf0'))

aux = Composite('Comp1')
aux.Add(Leaf('Leaf1'))
aux.Add(Leaf('Leaf2'))
root.Add(aux)

leaf3 = Leaf('Leaf3')
root.Add(leaf3)
root.Remove(leaf3)

# Start the operation
root.Operation()