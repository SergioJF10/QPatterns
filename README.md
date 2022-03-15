# Classical Patterns applied for hybrid operations
This repository contains several approaches trying to adapt the classical design patterns to sample dummy hybrid information systems, i.e., classical information systems that require some other sample and dummy quantum operations. The main goal of this repo is trying to fit the classic design patterns in information systems coexisiting with other quantum algorithms.

## Index
- Facade Pattern: `QFacade`. Example of the Facade Pattern for applying some Quantum Gates grouped.
- Flyweight Pattern: `QFlyweight`. Example of the Flyweigght Pattern for managing the client's use of systems for measuring superpositions.
- Proxy Pattern: `QProxy`. Example of the Proxy Pattern for managing the client's operation for measuring a superposition by means of a proxy who manages the RealSubject provider.
- Decorator Pattern: `QDecorator`. Example of the Decorator pattern for managing the functionality improvement for the basic Pauli gates in a dummy hybrid system.

## Languages & Integration
For implementing those hybrid dummy systems, we take advantage of the integration that Q# provides us for using hosts programs for calling the quantum operations written in Q#. As host language we will use Python.
