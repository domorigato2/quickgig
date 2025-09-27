# quantum_circuit.py
from qiskit import QuantumCircuit
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt

# Create a 2-qubit circuit
circuit = QuantumCircuit(2, 2)
circuit.h(0)  # Hadamard gate on qubit 0
circuit.cx(0, 1)  # CNOT gate (entangle qubits)
circuit.measure([0, 1], [0, 1])  # Measure both qubits
print(circuit)

# Simulate (requires matplotlib)
from qiskit_aer import AerSimulator
sim = AerSimulator()
job = sim.run(circuit, shots=1000)
result = job.result()
counts = result.get_counts()
print(counts)
plot_histogram(counts)
plt.show()