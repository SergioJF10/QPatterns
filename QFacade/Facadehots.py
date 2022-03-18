'''Module including all classes for simulating a hybrid system implementing the Facade Pattern for accessing Quantum operations'''

from ast import Sub
import qsharp
from QFacade import OpX, OpY, OpZ, OpH

class SubsystemX:
    '''Subsystem calling the Pauli X gate'''
    def DoX(self):
        print(OpX.simulate())

class SubsystemY:
    '''Subsytem calling the Pauli Y gate'''
    def DoY(self):
        print(OpY.simulate())

class SubsystemZ:
    '''Subsystem calling the Pauli Z gate'''
    def DoZ(self):
        print(OpZ.simulate())

class SubsystemH:
    '''Subsystem calling the H gate'''
    def DoH(self):
        print(OpH.simulate())

class Facade:
    def __init__(self):
        self.sX = SubsystemX()
        self.sY = SubsystemY()
        self.sZ = SubsystemZ()
        self.sH = SubsystemH()

    def DoPauli(self):
        print('Doing all Pauli Operations...')
        self.sX.DoX()
        self.sY.DoY()
        self.sZ.DoZ()

    def DoXnH(self):
        print('Doing PauliX gate and Hadamard gate...')
        self.sX.DoX()
        self.sH.DoH()

class Client:
    '''Client class for calling the Facade pattern operations'''
    def __init__(self, facade):
        self.facade = facade

    def Main(self):
        '''Main method'''
        self.facade.DoPauli()
        self.facade.DoXnH()

# MAIN
Client(Facade()).Main()