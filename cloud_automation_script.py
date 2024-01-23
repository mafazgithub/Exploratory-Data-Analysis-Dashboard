import boto3
import time

# Create an EC2 instance with detailed configurations
ec2 = boto3.resource('ec2', region_name='us-east-1')

instance = ec2.create_instances(
    ImageId='ami-0c55b159cbfafe1f0',  # Amazon Linux 2 AMI
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='your_key_pair_name',
    SecurityGroups=['your_security_group'],
    UserData='''#!/bin/bash
                echo "Hello from UserData script!" > /home/ec2-user/userdata_output.txt
              '''
)

# Wait for the instance to be running
instance[0].wait_until_running()

# Reload the instance attributes to get the updated public DNS
instance[0].load()
public_dns = instance[0].public_dns_name

# Print the public DNS of the created instance
print("Instance Public DNS:", public_dns)

# Sleep for a while to allow the instance to start up
time.sleep(30)

# Terminate the instance (cleanup)
instance[0].terminate()
    