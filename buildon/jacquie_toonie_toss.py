# honor of my friends at AWS Build On Weekly

from braket.circuits import Circuit
from braket.devices import LocalSimulator

toonie_toss_circuit = Circuit().h(0)
simulator = LocalSimulator()


task = simulator.run(toonie_toss_circuit, shots=100)

result = task.result()
if result.measurements[0][0] == 1:
    print("QEII!")
else:
    print("BEAR!")
