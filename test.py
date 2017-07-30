import boto3
client = boto3.client('ec2')
response = client.describe_instances()
for reservation in response['Reservations']:
        for instance in reservation['Instances']:
                instanceid = (instance['InstanceId'])
                print instanceid
