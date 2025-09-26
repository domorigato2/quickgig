# quantum_circuit.py
from qiskit import QuantumCircuit, transpile
from qiskit_aer import AerSimulator  # Try this, fallback if DLL fails
from qiskit.visualization import plot_histogram
import matplotlib.pyplot as plt
import sys
sys.stdout.reconfigure(encoding='utf-8')

circuit = QuantumCircuit(2, 2)
circuit.h(0)
circuit.cx(0, 1)
circuit.measure([0, 1], [0, 1])
print(circuit)

try:
    sim = AerSimulator()
    compiled_circuit = transpile(circuit, sim)
    job = sim.run(compiled_circuit, shots=1000)
    result = job.result()
    counts = result.get_counts()
    print(counts)
    plot_histogram(counts)
    plt.show()
except ImportError as e:
    print(f"Simulator error: {e}. Try basic circuit print only.")