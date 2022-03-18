'''Module including all the elements needed to implement the State behavioural pattern'''
import qsharp
from QuantumOperations import Entanglement, Superposition
from abc import ABC, abstractmethod

class Context:
    '''Class managing the current state and the transitions between Superposition and Entanglement states'''
    def __init__(self, initial):
        self.current = initial

    def Operation(self):
        '''Wrapper for calling the corresponding operation of the current state'''
        self.current.Operation()
    
    def Transition(self, next_state):
        '''Method for changing from one state to another'''
        self.current = next_state


class State(ABC):
    '''Abstract class representing the state of the system for the State pattern example'''
    def __init__(self):
        self.context = None
    
    @abstractmethod
    def SetContext(self, context):
        '''Setter method for setting in runtime the context object to be used'''
        pass

    @abstractmethod
    def Operation(self):
        '''Abstract method where the operation will call the real Quantum Operation'''
        pass

class ConcreteStateSuperposition(State):
    '''Concrete class implementing the State corresponding to the system calling Quantum superposition operation'''
    def __init__(self):
        super().__init__()

    def SetContext(self, context):
        '''Concrete method for setting the context to be used by the state'''
        self.context = context

    def Operation(self):
        '''Concrete method calling the superposition method'''
        print(f'[Superposition State] Result: {Superposition.simulate()}')
        # Create next state
        next_state = ConcreteStateEntanglement()
        next_state.SetContext(self.context)
        # Do transition
        self.context.Transition(next_state)

class ConcreteStateEntanglement(State):
    '''Concrete class implementing the State corresponding to the system calling Quantum entaglement operation'''
    def __init__(self):
        super().__init__()

    def SetContext(self, context):
        '''Concrete method for setting the context to be used by the state'''
        self.context = context

    def Operation(self):
        '''Concrete method calling the entanglement method'''
        print(f'[Entanglement State] Result: {Entanglement.simulate()}')
        # Create next state
        next_state = ConcreteStateSuperposition()
        next_state.SetContext(self.context)
        # Do transition
        self.context.Transition(next_state)

class Client:
    '''Client class for accessing the opertations defined in the pattern'''
    def Main(self):
        '''Main method'''
        # Create the instances
        superposition_state = ConcreteStateSuperposition()
        entanglement_state = ConcreteStateEntanglement()
        context = Context(superposition_state)
        # Set the contex object
        superposition_state.SetContext(context)
        entanglement_state.SetContext(context)
        # Testing operations
        for i in range(4): # 4 iterations 
            context.Operation()

# MAIN
Client().Main()