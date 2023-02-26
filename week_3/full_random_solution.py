# Use Braket SDK Cost Tracking to estimate the cost to run this example
from braket.tracking import Tracker
t = Tracker().start()


# part 1
# AWS imports: Import Braket SDK modules
from braket.circuits import Circuit
from braket.devices import LocalSimulator
from braket.aws import AwsDevice, AwsQuantumTask

# set up local simulator device
device = LocalSimulator()

# general math imports
import math, random
import numpy as np
from scipy.fft import fft, ifft

# magic word for producing visualizations in notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# import convex solver
import cvxpy as cp


# part 2  IonQ and Rigerri currently commented out
# set up Rigetti quantum device
#rigetti = AwsDevice("arn:aws:braket:us-west-1::device/qpu/rigetti/Aspen-M-3")

# set up IonQ quantum device
#ionq = AwsDevice("arn:aws:braket:::device/qpu/ionq/ionQdevice")

# simulator alternative: set up the on-demand simulator SV1
simulator = AwsDevice("arn:aws:braket:::device/quantum-simulator/amazon/sv1")


# part 3
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

# define circuit
n_qubits = 5
state = hadamard_circuit(n_qubits)

# print circuit
print(state)


# part 4


# run circuit
m_shots = 1
result = device.run(state, shots = m_shots).result()

# get measurement shots
counts = result.measurement_counts.keys()

# print counts
list_one = list(counts)[0]
array_one = np.array([list_one])
print("The output bit string is: ",array_one)


# part 5
# work with local simulator for testing Toeplitz construction
device = LocalSimulator()

# set security parameter
power = 8
eps = 10**(-power)
print(f"Security parameter: {eps}.")

# set number of output bits
m = 10
print(f"Desired output length: {m} bits.")

# set min-entropy rates for sources
k_1 = 0.8
print(f"Min-entropy rate of first source: {k_1}.")
k_2 = 0.8
print(f"Min-entropy rate of second source: {k_2}")

# required number of input bits (for each source)
n = math.floor((m-1-2*math.log2(eps))
    /(k_1+k_2-1))
print(f"Required length of each input source: {n} bits.")

# quantum circuit for generating weakly random bit string one
n1_qubits = 1
m1_shots = n
state1 = hadamard_circuit(n1_qubits)
result1 = device.run(state1, shots=m1_shots).result()
array_one = result1.measurements.reshape(1,m1_shots*n1_qubits)
# print(array_one)

# quantum circuit for generating weakly random bit string two
n2_qubits = 1
m2_shots = n
state2 = hadamard_circuit(n2_qubits)
result2 = device.run(state2, shots=m2_shots).result()
array_two = result2.measurements.reshape(1,m2_shots*n2_qubits)
# print(array_two)

###
# alternative for generating two bit strings when no quantum source is available:

# create first list of pseudo-random bits
# alternative when no quantum source is available
# list_one = []
# for number in range(n):
#    b = int(random.randint(0, 1))
#    list_one.append(b)
# array_one = np.array([list_one])

# create second list of pseudo-random bits
# list_two = []
# for number in range(n):
#    b = int(random.randint(0, 1))
#    list_two.append(b)
# array_two = np.array([list_two])
###

# computing output of Toeplitz extractor by vector-matrix multiplication
# via efficient Fast Fourier Transform (FFT) as discussed in [1]

# setting up arrays for FFT implementation of Toeplitz
array_two_under = np.array(array_two[0,0:n-m])[np.newaxis]
zero_vector = np.zeros((1,n+m-3), dtype=int)
array_two_zeros = np.hstack((array_two_under,zero_vector))
array_two_over = array_two[0,n-m:n][np.newaxis]
array_one_merged = np.zeros((1,2*n-3), dtype=int)
for i in range(m):
    array_one_merged[0,i] = array_one[0,m-1-i]
for j in range(n-m-1):
    array_one_merged[0,n+m-2+j] = array_one[0,n-2-j]

# FFT multplication output of Toeplitz
output_fft = np.around(ifft(fft(array_one_merged)*fft(array_two_zeros)).real)
output_addition = output_fft[0,0:m] + array_two_over
output_final = output_addition.astype(int) % 2
print(f"The {m} random output bits are:\n{output_final}.")


# part 6
# fix noise parameters
lamb = 0.02
mu = 0.98

# purification of rho input state
rho = 0.5*np.array([[1,1-lamb],[1-lamb,1]])
eigvals, eigvecs = np.linalg.eig(rho)

rho_vector =\
    math.sqrt(eigvals[0])*np.kron(eigvecs[:,0],eigvecs[:,0])[np.newaxis]\
    +math.sqrt(eigvals[1])*np.kron(eigvecs[:,1],eigvecs[:,1])[np.newaxis]
rho_pure = np.kron(rho_vector,rho_vector.T)

# sigma state of noisy measurement device
sigma_vector = np.array([[math.sqrt(1-mu),0,0,math.sqrt(mu)]])
sigma_pure = np.kron(sigma_vector,sigma_vector.T)

# omega state relevant for conditional min-entropy
rho_sigma = np.kron(rho_pure,sigma_pure)

id_2 = np.identity(2)
zero = np.array([[1,0]])
one = np.array([[0,1]])

zerozero = np.kron(np.kron(zero,id_2),np.kron(zero,id_2))
zeroone = np.kron(np.kron(zero,id_2),np.kron(one,id_2))
onezero = np.kron(np.kron(one,id_2),np.kron(zero,id_2))
oneone = np.kron(np.kron(one,id_2),np.kron(one,id_2))

omega_0 = zerozero@rho_sigma@zerozero.T+zeroone@rho_sigma@zeroone.T+onezero@rho_sigma@onezero.T
omega_1 = oneone@rho_sigma@oneone.T

omega = []
omega.append(omega_0)
omega.append(omega_1)

# sdp solver
m = 4 # dimension of quantum side information states
c = 2 # number of classical measurement outcomes

sigma = cp.Variable((m,m), complex=True) # complex variable
constraints = [sigma >> 0] # positive semi-definite
constraints += [sigma >> omega[i] for i in range(c)] # min-entropy constraints
obj = cp.Minimize(cp.real(cp.trace(sigma))) # objective function

prob = cp.Problem(obj,constraints) # set up sdp problem
prob.solve(solver=cp.SCS, verbose=True) # solve sdp problem using splitting conic solver (SCS)
guess = prob.value
qmin_entropy = (-1)*math.log2(guess)
min_entropy = 1-math.log2(2-mu*(1-lamb))

print("\033[1m" + "The coditional min-entropy is: ", qmin_entropy)
print("As a comparison, the unconditional min-entropy is: ", min_entropy)


# part 7
# set security parameter
power = 8
eps = 10**(-power)
print(f"Security parameter: {eps}.")

# set number of output bits
m = 10
print(f"Desired output length: {m} bits.")

# set min-entropy rates for sources - qmin_entropy from above
k_one = qmin_entropy
print(f"Min-entropy rate of first source: {k_1}.")
k_two = qmin_entropy
print(f"Min-entropy rate of second source: {k_2}.")

# required number of input bits (for each source)
n = math.floor((m-1-2*math.log2(eps))
    /(k_one+k_two-1))
print(f"Required length of each input source: {n} bits.")


# part 8
# running on the amazon sv simulator
# using Ion or Rigetti would require modifications of .run
n1_q = 1 # alternatively use more than one qubit (attention: 32 max + lower bounds on number of shots)
m1_s = int(math.ceil(n/n1_q))
state_simulator = hadamard_circuit(n1_q)
simulator_task = simulator.run(state_simulator, shots=m1_s, poll_timeout_seconds=5*24*60*60)

simulator_task_id = simulator_task.id
simulator_status = simulator_task.state()
print("Status of simulator task:", simulator_status)


# part 9
# recover simulator task
task_load_simulator = AwsQuantumTask(arn=simulator_task_id)

# print status
status_simulator = task_load_simulator.state()
print('Status of simulator task:', status_simulator)
# wait for job to complete
# terminal_states = ['COMPLETED', 'FAILED', 'CANCELLED']
if status_simulator == 'COMPLETED':
    # get results
    simulator_results = task_load_simulator.result()

    # array
    array_simulator = simulator_results.measurements.reshape(1,m1_s*n1_q)
    print("The first raw bit string is: ",array_simulator)

elif status_simulator in ['FAILED', 'CANCELLED']:
    # print terminal message
    print('Your simulator task is in terminal status, but has not completed.')

else:
    # print current status
    print('Sorry, your simulator task is still being processed and has not been finalized yet.')


# part 10
# code assumes calls to Ion and Rigetti and not SV hence the pair of if / else statements
# setting up arrays for fft implementation of Toeplitz
if status_simulator == 'COMPLETED':
    array_two_under = np.array(array_simulator[0,0:n-m])[np.newaxis]
    zero_vector = np.zeros((1,n+m-3), dtype=int)
    array_two_zeros = np.hstack((array_two_under,zero_vector))
    array_two_over = array_simulator[0,n-m:n][np.newaxis]
    array_one_merged = np.zeros((1,2*n-3), dtype=int)
    if status_simulator == 'COMPLETED':
        for i in range(m):
            array_one_merged[0,i] = array_simulator[0,m-1-i]
        for j in range(n-m-1):
            array_one_merged[0,n+m-2+j] = array_simulator[0,n-2-j]

        # fft multplication output of Toeplitz
        output_fft = np.around(ifft(fft(array_one_merged)*fft(array_two_zeros)).real)
        output_addition = output_fft[0,0:m] + array_two_over
        output_final = output_addition.astype(int) % 2
        print(f"The {m} random output bits are:\n{output_final}.")
    else:
        print(f"Your simulator task is in {status_simulator} state.")
else:
    print(f"Your simulator task is in {status_simulator} state.")


# part 11
# this associates to the first line where we track the task and the costs
# it will print a summary of the job details and the cost to execute it
print("Task Summary")
print(t.quantum_tasks_statistics())
print('Note: Charges shown are estimates based on your Amazon Braket simulator and quantum processing unit (QPU) task usage. Estimated charges shown may differ from your actual charges. Estimated charges do not factor in any discounts or credits, and you may experience additional charges based on your use of other services such as Amazon Elastic Compute Cloud (Amazon EC2).')
print(f"Estimated cost to run this example: {t.qpu_tasks_cost() + t.simulator_tasks_cost():.2f} USD")


# end of script
