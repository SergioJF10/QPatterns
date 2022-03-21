namespace QuantumOperation {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation QuantumAlg(): (Result, Result) {
         // A HUGE TIME CONSUMING ALGORITHM...
        use (q1, q2) = (Qubit(), Qubit());
        H(q1);
        CNOT(q1, q2);
        return (M(q1), M(q2));
    }
}
