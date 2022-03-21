# Classical Patterns applied for hybrid operations
This repository contains several approaches trying to adapt the classical design patterns to sample dummy hybrid information systems, i.e., classical information systems that require some other sample and dummy quantum operations. The main goal of this repo is trying to fit the classic design patterns in information systems coexisiting with other quantum algorithms.

## Index
- Structural Patterns
   - Facade Pattern: [`QFacade`](https://github.com/SergioJF10/QPatterns/tree/main/QFacade). Example of the Facade Pattern for applying some Quantum Gates grouped.
   - Flyweight Pattern: [`QFlyweight`](https://github.com/SergioJF10/QPatterns/tree/main/QFlyweight). Example of the Flyweigght Pattern for managing the client's use of systems for measuring superpositions.
   - Proxy Pattern: [`QProxy`](https://github.com/SergioJF10/QPatterns/tree/main/QProxy). Example of the Proxy Pattern for managing the client's operation for measuring a superposition by means of a proxy who manages the RealSubject provider.
   - Decorator Pattern: [`QDecorator`](https://github.com/SergioJF10/QPatterns/tree/main/QDecorator). Example of the Decorator pattern for managing the functionality improvement for the basic Pauli gates in a dummy hybrid system.
   - Composite Pattern: [`QComposite`](https://github.com/SergioJF10/QPatterns/tree/main/QComposite). Example of the Composite pattern for ordering a set of functionalities and executing them as a "_operational thread_".
- Behavioral Patterns
   - State Pattern: [`QState`](https://github.com/SergioJF10/QPatterns/tree/main/QState). Example of the State pattern for managing the execution of quantum operations according to the corresponding state and its transitions.
   - Observer Pattern: [`QObserver`](https://github.com/SergioJF10/QPatterns/tree/main/QObserver). Example of the Observer pattern for managing the observers' updates from a subject running heavy quantum algorithms.
- Other folders
   - Documentation: [`doc`](). Contains documentation files for the all the projects in this repository
      - Diagrams: [`UML_Diagrams`](). Visual Paradigm (.vpp) files containing the UML class diagrams of the previous examples.
      - PDF Doc.: [`Documentation`](). PDF (.pdf) file containing a textual explanation of the previous examples in the repository.

## Languages & Integration
For implementing those hybrid dummy systems, we take advantage of the integration that Q# provides us for using hosts programs for calling the quantum operations written in Q#. As host language we will use Python. For more information, visit this [link](https://docs.microsoft.com/es-es/azure/quantum/user-guide/host-programs?tabs=tabid-python#q-with-host-programs) with Microsoft's documentation about how to run a Q# program.
