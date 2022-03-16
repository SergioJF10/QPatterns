namespace QuantumGates {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation OpX(): Result {
        use q = Qubit();
        X(q);
        return M(q);
    }

    operation Entanglement(): (Result, Result) {
        use (q1, q2) = (Qubit(), Qubit());
        // Get entanglement
        H(q1);
        CNOT(q1, q2);
        // Return measurement of both qubits
        return (M(q1), M(q2));
    }
}