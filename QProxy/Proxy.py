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
        print(QProxy.Request.simulate())

class Proxy(Subject):
    '''Proxy for requesting the RealSubject'''

    realSubj = None

    def Request(self):
        '''Proxy middle Request'''
        if self.realSubj is None:
            self.realSubj = RealSubject()
        
        self.realSubj.Request()

class Client:
    '''Client asking for the request'''

    subj = Proxy()

    def DoRequest(self):
        self.subj.Request()


## MAIN
client = Client()
client.DoRequest()