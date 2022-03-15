namespace QProxy {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation Request() : Result {
        // Real Quantum Requested Operation Implementation
        use q = Qubit();
        H(q);
        return M(q);
    }
}
