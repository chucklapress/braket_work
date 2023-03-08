
# step 1
from braket.circuits import Circuit, Gate, Moments
from braket.circuits.instruction import Instruction
from braket.aws import AwsDevice
from braket.devices import LocalSimulator
import matplotlib.pyplot as plt
import time


# step 2
# Set up device: local simulator or the ionq device
#device = LocalSimulator()
device = AwsDevice("arn:aws:braket:::device/qpu/ionq/ionQdevice")


# step 3
# Function to run quantum task, check the status thereof and collect results
def get_result(device, circ):

    # get number of qubits
    num_qubits = circ.qubit_count

    # specify desired results_types
    circ.probability()

    # submit task: define task (asynchronous)
    if device.name == 'LocalSimulator':
        task = device.run(circ, shots=100)
    else:
        task = device.run(circ, shots=100)

    # Get ID of submitted task
    task_id = task.id
#     print('Task ID :', task_id)

    # Wait for job to complete
    status_list = []
    status = task.state()
    status_list += [status]
    print('Status:', status)

    # Only notify the user when there's a status change
    while status != 'COMPLETED':
        status = task.state()
        if status != status_list[-1]:
            print('Status:', status)
        status_list += [status]

    # get result
    result = task.result()

    # get metadata
    metadata = result.task_metadata

    # get output probabilities
    probs_values = result.values[0]

    # get measurement results
    measurement_counts = result.measurement_counts

    # print measurement results
    print('measurement_counts:', measurement_counts)

    # bitstrings
    format_bitstring = '{0:0' + str(num_qubits) + 'b}'
    bitstring_keys = [format_bitstring.format(ii) for ii in range(2**num_qubits)]

    # plot probabalities
    plt.bar(bitstring_keys, probs_values)
    plt.xlabel('bitstrings')
    plt.ylabel('probability')
    plt.xticks(rotation=90)
    plt.show()

    return measurement_counts


# step 4


circ = Circuit()
circ.h([0])
circ.cnot(0,1)


# step 5


# Four possible messages and their corresponding gates
message = {"00": Circuit().i(0),
           "01": Circuit().x(0),
           "10": Circuit().z(0),
           "11": Circuit().x(0).z(0)
          }


# step 6


# Select message to send.  11 selected for this run
m = "11"


# step 7


# Encode the message
circ.add_circuit(message[m])


# step 8


circ.cnot(0,1)
circ.h([0])


# step 9


print(circ)


# step 10


counts = get_result(device, circ)
print(counts)


# end of program
