'''Module including all the implementations needed for simulating Observer Pattern'''

import qsharp
import time
from abc import ABC, abstractmethod
from QuantumOperation import QuantumAlg

class Observer(ABC):
    '''Abstract class representing an observer interested in a subject update'''
    def Update(self):
        '''Abstract method for being notified by any subject instance'''
        pass

class ConcreteObserver(Observer):
    '''Implementation of the Observer class'''
    def __init__(self, name):
        self.name = name
        self.subState = 0

    def SetSubject(self, sub):
        '''Setter for indicating the ConcreteSubject instance'''
        self.subject = sub

    def Update(self):
        '''Implementation of the Update abstract method'''
        self.subState = self.subject.GetState()
        print(f'[Observer {self.name}] Notification received, subState = {self.subState}')

class QuantumSubject(ABC):
    '''Abstract class representing the subject providing an interface for managing observers'''
    @abstractmethod
    def Attach(self, obs):
        '''Abstract method for adding a new observer to the list'''
        pass

    @abstractmethod
    def Detach(self, obs):
        '''Abstract method for removing an observer from the list'''
        pass

    @abstractmethod
    def Notify(self):
        '''Abstract method for notifying each observer in the list about a change'''
        pass

class ConcreteQSubject(QuantumSubject):
    '''Implementation of the Subject class'''
    def __init__(self, name):
        self.name = name
        self.observers = []
        self.state = 0 # state = number of quantum operations performed

    def Attach(self, obs):
        '''Implementation of the Attach method from the abstract class'''
        self.observers.append(obs)

    def Detach(self, obs):
        '''Implementation of the Detach method from the abstract class'''
        self.observers.remove(obs)

    def Notify(self):
        '''Implementation of the Notify method from the abstract class'''
        for obs in self.observers:
            print(f'[Subject {self.name}] Notifying Obs {obs.name}')
            obs.Update()

    def Operation(self):
        '''Method for calling and simulating a huge Quantum Algorithm'''
        print(f'[Subject {self.name}] Performing operation #{self.state}...')
        # Simulating huge quantum algorithm
        time.sleep(3); print(f'[Subject {self.name}] Quantum Algorithm Result: {QuantumAlg.simulate()}')
        self.state += 1
        self.Notify()

    def GetState(self):
        '''Getter method for returning the state's value'''
        return self.state

class Client:
    '''Client class for calling the operations of the Observer pattern'''
    def __init__(self, subject):
        self.subj = subject

    def Main(self):
        '''Main method'''
        obs1 = ConcreteObserver('Obs1')
        obs1.SetSubject(self.subj)
        obs2 = ConcreteObserver('Obs2')
        obs2.SetSubject(self.subj)
        obs3 = ConcreteObserver('Obs3')
        obs3.SetSubject(self.subj)

        self.subj.Attach(obs1)
        self.subj.Attach(obs2)
        self.subj.Attach(obs3)
        self.subj.Detach(obs3)

        self.subj.Operation()


## MAIN
Client(ConcreteQSubject('Sub1')).Main()
