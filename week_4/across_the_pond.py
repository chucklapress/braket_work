# part 1
import boto3
from braket.aws import AwsDevice
from braket.devices import LocalSimulator
from braket.circuits import Circuit

# create the circuit
bell = Circuit().h(0).cnot(0, 1)
print(bell)

# part 2
# instantiate the local simulator
local_sim = LocalSimulator()
# run the circuit
result = local_sim.run(bell, shots=1000).result()
counts = result.measurement_counts
print(counts)

# part 3
# get the account ID
aws_account_id = boto3.client("sts").get_caller_identity()["Account"]
# the name of the bucket
# setting the s3 bucket to collect the run results in the London UK region
# replace xxxxxxxxxxxx value with your aws acct 
my_bucket = "amazon-braket-eu-west-2-xxxxxxxxxxxx"
# the name of the folder in the bucket
my_prefix = "simulation-output"
s3_folder = (my_bucket, my_prefix)

# part 4
# choose the cloud-based on-demand simulator to run your circuit
device = AwsDevice("arn:aws:braket:eu-west-2::device/qpu/oqc/Lucy")

# execute the circuit
task = device.run(bell, s3_folder, shots=100)
# display the results
print(task.result().measurement_counts)
