namespace Superposition {
    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;

    operation MeasureSuperposition(): Result {
        use q = Qubit();
        H(q);
        return M(q);
    }
}