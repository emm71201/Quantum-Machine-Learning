import cirq
import matplotlib.pyplot as plt
import numpy as np

# define qubit
qubit = cirq.GridQubit(0, 0)
# create a circuit
circuit = cirq.Circuit([cirq.H(qubit), cirq.measure(qubit, key='m')])
print("Circuit Follows")
print(circuit)
sim = cirq.Simulator()
output = sim.run(circuit, repetitions=100)
print("Measurement Output")
print(output)
print("Histogram of Measurement Output")
print(output.histogram(key="m"))
prob = []
for rep in np.array(range(1, 100)):
    output = sim.run(circuit, repetitions=rep)
    probs = output.histogram(key="m")
    prob.append(probs[0]/rep)
plt.plot(prob)
plt.show()

# Bell state creation
# two qubits on linequbit
q_register = [cirq.LineQubit(i) for i in range(2)]
# hadamard gate on 0 and cnot with target 1
circuit = cirq.Circuit([cirq.H(q_register[0]), cirq.CNOT(q_register[0]\
                                                         , q_register[1]), cirq.measure(*q_register, key="z")])
print("Bell State circuit\n", circuit)
output = sim.run(circuit, repetitions=100)
print(output.histogram(key="z"))