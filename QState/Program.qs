namespace QuantumOperations {
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Canon;

    operation Entanglement(): (Result, Result) {
        use (q1, q2) = (Qubit(), Qubit());
        // Entangle the qubits
        H(q1);
        CNOT(q1, q2);
        // Return a measurement
        return (M(q1), M(q2));
    }
    
    operation Superposition(): Result {
        use q = Qubit();
        // Create superposition
        H(q);
        // Return a measurement
        return M(q);
    }
}
