
# step 1

from braket.ahs.hamiltonian import Hamiltonian
from braket.ahs.atom_arrangement import AtomArrangement
from braket.ahs.analog_hamiltonian_simulation import AnalogHamiltonianSimulation

register = AtomArrangement()
H = Hamiltonian()

ahs_program = AnalogHamiltonianSimulation(
    hamiltonian=H,
    register=register
)


# step 2
import numpy as np
import matplotlib.pyplot as plt
# e.g. three atoms in an equilateral triangle, with pairwise
# separation equal to 5.5 micrometers
a = 5.5e-6  # meters

register.add([0, 0])
register.add([a, 0.0])
register.add([0.5 * a, np.sqrt(3)/2 * a]);


# srep 3

from braket.timings.time_series import TimeSeries
from braket.ahs.driving_field import DrivingField

# e.g. trapzoid amplitude time series
Omega_max = 2.5e6  # rad / seconds

# e.g. the duration of the program
t_max = np.pi/(np.sqrt(2)*Omega_max) # seconds

# e.g. constant Rabi frequency
Omega = TimeSeries()
Omega.put(0.0, Omega_max)
Omega.put(t_max, Omega_max)

# e.g. all-zero phase and detuning
phi = TimeSeries().put(0.0, 0.0).put(t_max, 0.0)  # (time [s], value [rad])
Delta_global = TimeSeries().put(0.0, 0.0).put(t_max, 0.0)  # (time [s], value [rad/s])

drive = DrivingField(
    amplitude=Omega,
    phase=phi,
    detuning=Delta_global
)

H += drive


# step 4

from braket.ahs.field import Field
from braket.ahs.pattern import Pattern
from braket.ahs.shifting_field import ShiftingField

# e.g. constant strong shifting field
Delta_local = TimeSeries()
Delta_local.put(0.0, -Omega_max*20)  # (time [s], value [rad/s])
Delta_local.put(t_max, -Omega_max*20)


# e.g. the shifting field only acts on the third atom,
# which is the top atom in the triangular array.
h = Pattern([0, 0, 0.5])

shift = ShiftingField(
    magnitude=Field(
        time_series=Delta_local,
        pattern=h
    )
)

H += shift


# step 5
pip install quera-ahs-utils


# step 6

ahs_program.to_ir().dict()


# step 7


from braket.devices import LocalSimulator
device = LocalSimulator("braket_ahs")


# step 8


result = device.run(ahs_program, shots=1000).result()


# step 9


def get_counters_from_result(result):
    post_sequences = [list(measurement.post_sequence) for measurement in result.measurements]
    post_sequences = ["".join(['r' if site==0 else 'g' for site in post_sequence]) for post_sequence in post_sequences]

    counters = {}
    for post_sequence in post_sequences:
        if post_sequence in counters:
            counters[post_sequence] += 1
        else:
            counters[post_sequence] = 1
    return counters

get_counters_from_result(result)


# step 10


from braket.ahs.atom_arrangement import AtomArrangement
import numpy as np
from quera_ahs_utils.plotting import show_register

a = 6.1e-6  # meters
N_atoms = 11

register = AtomArrangement()
for i in range(N_atoms):
    register.add([0.0, i*a])

fig = show_register(register)

# step 11

from braket.ahs.hamiltonian import Hamiltonian

H = Hamiltonian()


# step 12


from quera_ahs_utils.plotting import show_global_drive
from quera_ahs_utils.drive import get_drive

omega_min = 0
omega_max = 2.5e6 * 2 * np.pi
detuning_min = -9e6 * 2 * np.pi
detuning_max = 7e6 * 2 * np.pi

time_max = 4e-6
time_ramp = 0.15*time_max

time_points = [0, time_ramp, time_max - time_ramp, time_max]
omega_values = [omega_min, omega_max, omega_max, omega_min]
detuning_values = [detuning_min, detuning_min, detuning_max, detuning_max]
phase_values = [0, 0, 0, 0]

drive = get_drive(time_points, omega_values, detuning_values, phase_values)
H += drive

show_global_drive(drive)


# step 13


from braket.ahs.analog_hamiltonian_simulation import AnalogHamiltonianSimulation

ahs_program = AnalogHamiltonianSimulation(
    register=register,
    hamiltonian=H
)


# step 14


from braket.devices import LocalSimulator

classical_device = LocalSimulator("braket_ahs")

nshots = 1000
task = classical_device.run(ahs_program, shots=nshots)

# The result can be downloaded directly into an object in the python session:
result = task.result()


# step 15


from quera_ahs_utils.analysis import get_avg_density
from quera_ahs_utils.plotting import plot_avg_density

n_rydberg = get_avg_density(result)
plot_avg_density(n_rydberg, register)
plt.show()


# current end of program
# next would be running the program on the actual hardware
