namespace QFacade {

    open Microsoft.Quantum.Canon;
    open Microsoft.Quantum.Intrinsic;
    open Microsoft.Quantum.Diagnostics;

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

    operation OpH(): Result {
        use q = Qubit();
        H(q);
        return M(q);
    }
}
