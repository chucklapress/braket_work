# part 1

import boto3
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


# part 3


# get the account ID
aws_account_id = boto3.client("sts").get_caller_identity()["Account"]
# the name of the bucket account number obscured 
my_bucket = "amazon-braket-us-west-1-xxxxxxxxxxxx"
# the name of the folder in the bucket
my_prefix = "simulation-output"
s3_folder = (my_bucket, my_prefix)


# part 4 not shots increased to 10 as rigetti min shot number


# choose the cloud-based on-demand simulator to run your circuit
device = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Aspen-M-3")

# define circuit
n_qubits = 5
state = hadamard_circuit(n_qubits)
# print circuit
print(state)

# run circuit
m_shots = 10
task = device.run(state, s3_folder, shots= m_shots)
result = task.result()

# get measurement shots
counts = result.measurement_counts.keys()

# print counts actually produces 10 lsts but I only print 8
list_one = list(counts)[0]
list_two = list(counts)[1]
list_three = list(counts)[2]
list_four = list(counts)[3]
list_five = list(counts)[4]
list_six = list(counts)[5]
list_seven = list(counts)[6]
list_eight = list(counts)[7]
array_one = np.array([list_one,list_two,list_three,list_four,list_five,list_six,list_seven,list_eight])
print("The output bit string is: ",array_one)


# end of script
