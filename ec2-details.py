import boto3 as boto

client = boto.client('ec2')
ec2_response = client.describe_instances()

ec2 = ec2_response["Reservations"]
#print(type(response))
#print(type(ec2))
for dic in ec2:
	instances = dic["Instances"]
	for instance in instances:
		AZ_details = instance["Placement"]
		print("Instance ID: " + instance["InstanceId"] + " \n Avilability Zone: " + AZ_details["AvailabilityZone"])

