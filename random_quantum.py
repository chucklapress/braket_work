# part 1


# AWS imports: Import Braket SDK modules
from braket.circuits import Circuit
from braket.aws import AwsDevice
from braket.devices import LocalSimulator
import numpy as np

# set up local simulator device
device = LocalSimulator()

# function for Hadamard cirquit
def hadamard_circuit(n_qubits):
    """
    function to apply Hadamard gate on each qubit
    input: number of qubits
    """

    # instantiate circuit object
    circuit = Circuit()

    # apply series of Hadamard gates
    for i in range(n_qubits):
        circuit.h(i)
    return circuit


# part 2


# define circuit
n_qubits = 5
state = hadamard_circuit(n_qubits)
# print circuit
print(state)

# run circuit
m_shots = 1
result = device.run(state, shots = m_shots).result()

# get measurement shots
counts = result.measurement_counts.keys()

# print counts
list_one = list(counts)[0]
array_one = np.array([list_one])
print("The output bit string is: ",array_one)


# end of program
