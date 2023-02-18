# step 1

pip install qiskit-braket-provider pylatexenc


# step 2
import qiskit_braket_provider


# step 3
from qiskit import QuantumCircuit
circuit = QuantumCircuit(3)
circuit.h(0)
for qubit in range(1, 3):
    circuit.cx(0, qubit)


# step 4
circuit.draw('mpl')


# step 5
from qiskit_braket_provider import BraketLocalBackend
local_simulator = BraketLocalBackend()
task = local_simulator.run(circuit, shots=1000)


# step 6
from qiskit.visualization import plot_histogram
plot_histogram(task.result().get_counts())


# running on rigetti quantum computer
# step 1
from qiskit_braket_provider import AWSBraketProvider
provider = AWSBraketProvider()
rigetti_device = provider.get_backend("Aspen-M-3")


# step 2
rigetti_task = rigetti_device.run(circuit, shots=100)
rigetti_retrieved = rigetti_device.retrieve_job(job_id=rigetti_task.job_id())
rigetti_retrieved.status()

# expected outcome
"""
<JobStatus.RUNNING: 'job is actively running'>
"""
# step 3
rigetti_retrieved.status()
# expected outcome
"""
<JobStatus.DONE: 'job has successfully run'>
"""

# step 4

plot_histogram(retrieved_job.result().get_counts())

"""
Credit to Jordan Sullivan post https://aws.amazon.com/blogs/quantum-computing/introducing-the-qiskit-provider-for-amazon-braket/
"""
