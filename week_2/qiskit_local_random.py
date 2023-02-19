# import into notebook
pip install qiskit-braket-provider pylatexenc


# Step 1
import random
import qiskit
from qiskit import QuantumCircuit, execute
from qiskit_braket_provider import BraketLocalBackend

# Step 2
local_simulator = BraketLocalBackend()

# Define the quantum circuit
circuit = QuantumCircuit(4, 4)
circuit.h(range(4))
circuit.measure(range(4), range(4))

# step 3
binary_strings = []

for i in range(10):
    # Execute the circuit on the backend
    job = local_simulator.run(circuit, shots=10)

    # Get the results from the job
    result = job.result()

    # Convert the output to a binary string
    binary_string = "".join([str(bit) for bit in result.get_counts().keys()][0])

    # Check if the number is already in the list
    if binary_string not in binary_strings:
        binary_strings.append(binary_string)
    else:
        i -= 1

# Print the binary strings
print(binary_strings)

circuit.draw('mpl')

"""
The addition of the rigetti quantom machine
"""
from qiskit_braket_provider import AWSBraketProvider
provider = AWSBraketProvider()
rigetti_device = provider.get_backend("Aspen-M-3")

binary_strings = []
rigetti_task = rigetti_device.run(circuit, shots=10)
for i in range(10):
    # Execute the circuit on the backend
    job = rigetti_task

    # Get the results from the job
    result = job.result()

    # Convert the output to a binary string
    binary_string = "".join([str(bit) for bit in result.get_counts().keys()][0])

    # Check if the number is already in the list

    if binary_string not in binary_strings:
        binary_strings.append(binary_string)
    else:
        i -= 1

rigetti_retrieved = rigetti_device.retrieve_job(job_id=rigetti_task.job_id())
rigetti_retrieved.status()

"""
when job completed successfully
"""
# this will provide a visualization of the results of your run
from qiskit.visualization import plot_histogram
plot_histogram(job.result().get_counts())

# lastly print counts to notebook
print(job.result().get_counts())
