### Pulse control and openqasm
The purpose of this focus of code and learning is in understanding control of the hardware from both
utilizing the OpenQASM programming lanquage  
Open Quantum Assembly Language (OpenQASM) is a programming language designed for describing quantum circuits and algorithms for execution on quantum computers.  
The language includes a mechanism for describing explicit timing of instructions, and allows for the attachment of low-level definitions to gates for tasks such as calibration.  

Pulse Control allows us to refine device-level quantum control to become fault tolerant, and is the programatic middle ground until more refined quantum hardware is a reality. 

#### currently capturing  
currently learning about lower level pulse control using frames and ports  
[AWS Hello Pulse](https://docs.aws.amazon.com/braket/latest/developerguide/braket-hello-pulse.html)  
[AWS Blog post](https://aws.amazon.com/blogs/quantum-computing/amazon-braket-launches-braket-pulse-to-develop-quantum-programs-at-the-pulse-level/)  
[On Frames and Ports](https://docs.aws.amazon.com/braket/latest/developerguide/braket-roles-frames-ports.html)  

#### added pulse_result.json  
added result.json from actual run on Rigetti hardware, you can see by the results the specified Qubits that were called the pulse and the results of the run.


#### video discussing pulse control, why it's even a thing. This is from IBM and discuss Qiskit but the concept is still applicable  

[![IMAGE ALT TEXT](img/pulse.png)](https://www.youtube.com/watch?v=ZvipHRY-URs)  
