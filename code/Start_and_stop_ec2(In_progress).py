import boto3

ec2_resource = boto3.resource("ec2")

x = ec2_resource.create_instances(ImageId = 'ami-0cff7528ff583bf9a',
      InstanceType = 't2.micro',
      MaxCount = 1,
      MinCount = 1,#change counts to add multiple
      TagSpecifications = [
                           {
                               'ResourceType': 'instance',
                               'Tags': [{'Key': 'Test1','Value': 'Test1pair'}]
                           },
                       ],
                       )

print(x)

x = ec2_resource.create_instances(ImageId = 'ami-0cff7528ff583bf9a',
      InstanceType = 't2.micro',
      MaxCount = 1,
      MinCount = 1,#change counts to add multiple
      TagSpecifications = [
                           {
                               'ResourceType': 'instance',
                               'Tags': [{'Key': 'Test2','Value': 'Test2pair'}]
                           },
                       ],
                       )
      
ec2 = boto3.resource('ec2')

for i in response['Instances']:
    print("Instance ID Created is :{} Instance Type Created is : {}" .format(i['InstanceId'],i['InstanceType']))
ec2_client = boto3.client("ec2")

instances = ec2.instances.filter(
Filters=[{'Name': 'instance-state-name', 'Values': ['running']}])

for instance in instances:
    print(instance.id, instance.instance_type)
 
import boto3
ec2_client=boto3.client("ec2")

x=ec2_client.describe_instances()

data=x["Reservations"]

li=[]
for instances in data:
    instance=instances["Instances"]
    for ids in instance:
        instance_id=ids["InstanceId"]
        li.append(instance_id)
        
#ec2_client.terminate_instances(InstanceIds=li)
print(instance_id)