awsservices = []

awsservices += ['ec2', 'lambda', 'cloudtrail', 'cloudwatch', 's3']

print(awsservices)

print("The length of this list is ", len(awsservices))

del awsservices [:2:4]

print(awsservices)

print("The length of this list is ", len(awsservices))

