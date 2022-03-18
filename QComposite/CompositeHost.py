'''Module with all the elements needed for implementing a dummy sample hybrid information system applying the Composite Pattern'''

import qsharp
from QuantumGates import OpX, Entanglement
from abc import ABC, abstractmethod

class TreeComponent(ABC):
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

class Composite(TreeComponent):
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
        print(f'[Composite {self.name}] Pauli Y Result: {Entanglement.simulate()}')

        for child in self.children:
            print('\t', end="")
            child.Operation()

class Leaf(TreeComponent):
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

class Client:
    '''Client class for calling the operations of the Composite Pattern'''
    def __init__(self):
        self.root = Composite('Root')

    def Main(self):
        '''Main method'''
        self.root.Add(Leaf('Leaf0'))

        aux = Composite('Comp1')
        aux.Add(Leaf('Leaf1'))
        aux.Add(Leaf('Leaf2'))
        self.root.Add(aux)

        leaf3 = Leaf('Leaf3')
        self.root.Add(leaf3)
        self.root.Remove(leaf3)

        # Start the operation
        self.root.Operation()

# MAIN
Client().Main()