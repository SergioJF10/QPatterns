'''Module including necessary classes and methods for a Proxy Pattern wrapping a Quantum Operation'''

from abc import ABC, abstractmethod
import qsharp
import QProxy

class Subject(ABC):
    '''Abstract Subject Class'''
    @abstractmethod
    def Request(self):
        pass

class RealSubject(Subject):
    '''Real Subject Class who contains the Quantum Logic'''

    def Request(self):
        '''Quantum Logic Call'''
        print(f'[RealSubject] Quantum Algorithm Result: {QProxy.Request.simulate()}')

class Proxy(Subject):
    '''Proxy for requesting the RealSubject'''
    def __init__(self):
        self.realSubj = None

    def Request(self):
        '''Proxy middle Request'''
        if self.realSubj is None:
            self.realSubj = RealSubject()
        
        print('[Proxy] Calling RealSubject.Request()')
        self.realSubj.Request()

class Client:
    '''Client asking for the request'''
    def __init__(self, subj):
        self.subj = subj

    def Main(self):
        '''Main method'''
        self.subj.Request()


## MAIN
Client(Proxy()).Main()