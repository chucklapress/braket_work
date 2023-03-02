# part 1
pip install quera-ahs-utils

# part 2

from braket.ahs.atom_arrangement import AtomArrangement
import numpy as np
from quera_ahs_utils.plotting import show_register
import matplotlib.pyplot as plt

a = 6.1e-6  # meters
N_atoms = 11

register = AtomArrangement()
for i in range(N_atoms):
    register.add([0.0, i*a])

fig = show_register(register)
plt.show()

# part 3

from braket.ahs.hamiltonian import Hamiltonian

H = Hamiltonian()


# part 4


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
plt.show()


# part 5


from braket.ahs.analog_hamiltonian_simulation import AnalogHamiltonianSimulation

ahs_program = AnalogHamiltonianSimulation(
    register=register,
    hamiltonian=H
)


# part 6


from braket.devices import LocalSimulator

classical_device = LocalSimulator("braket_ahs")

nshots = 100
task = classical_device.run(ahs_program, shots=nshots)

# The result can be downloaded directly into an object in the python session:
result = task.result()


# part 7


from quera_ahs_utils.analysis import get_avg_density
from quera_ahs_utils.plotting import plot_avg_density

n_rydberg = get_avg_density(result)
fig,ax = plot_avg_density(n_rydberg, register,cmap=plt.cm.Blues)
plt.show()


# part 8


b = 6.7e-6  # meters
N_x = N_y = 3

register_2D = AtomArrangement()
for i in range(N_x):
    for j in range(N_y):
        register_2D.add([i*b, j * b])

show_register(register_2D)
plt.show()


# part 9


H_2D = Hamiltonian()

omega_min = 0
omega_max = 2.5e6 * 2 * np.pi
detuning_min = -8.75e6 * 2 * np.pi
detuning_max = 8.75e6 * 2 * np.pi

time_max = 3e-6
time_ramp = 0.25e-6

time_points = [0, time_ramp, time_max - time_ramp, time_max]
omega_values = [omega_min, omega_max, omega_max, omega_min]
detuning_values = [detuning_min, detuning_min, detuning_max, detuning_max]
phase_values = [0, 0, 0, 0]

drive_2D = get_drive(time_points, omega_values, detuning_values, phase_values)
H_2D += drive_2D


# part 10


ahs_program_2D = AnalogHamiltonianSimulation(
    register=register_2D,
    hamiltonian=H_2D
)

result_2D = classical_device.run(ahs_program_2D, shots=nshots).result()

f,ax = plot_avg_density(get_avg_density(result_2D), register_2D, cmap=plt.cm.Blues)
plt.show()


# part 11


b = 6.7e-6  # meters
N_x = N_y = 11

register_finale = AtomArrangement()
for i in range(N_x):
    for j in range(N_y):
        register_finale.add([j*b, i * b])


# part 12


ahs_program_finale = AnalogHamiltonianSimulation(
    register=register_finale,
    hamiltonian=H_2D
)

result_2D = classical_device.run(ahs_program_2D, shots=nshots).result()
plot_avg_density(get_avg_density(result_2D), register_2D, cmap=plt.cm.Blues);
plt.show()


# end still haven't used actual hardware
