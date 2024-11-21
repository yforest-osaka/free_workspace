from qulacs import QuantumState, QuantumCircuit
from qulacs.gate import X, Y, Z, H, CNOT, CZ
from time import time

def main():
    nqubits = 30
    sample_circuit = QuantumCircuit(nqubits)
    for i in range(nqubits):
        sample_circuit.add_H_gate(i)
    # for i in range(nqubits):
    #     sample_circuit.add_CNOT_gate(i, (i+1)%nqubits)

    state = QuantumState(nqubits)

    start = time()
    sample_circuit.update_quantum_state(state)
    end = time()
    print(f"Time: {end - start}") 

if __name__ == "__main__":
    main()

