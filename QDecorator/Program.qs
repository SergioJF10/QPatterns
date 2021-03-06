namespace QuantumComponents {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation OpX(): Result {
        use q = Qubit();
        X(q);
        return M(q);
    }

    operation OpY(): Result {
        use q = Qubit();
        Y(q);
        return M(q);
    }

    operation OpZ(): Result {
        use q = Qubit();
        Z(q);
        return M(q);
    }
}