''' create new spot ec2 instance module '''
import boto3


ec2 = boto3.resource('ec2', region_name='us-east-1')


# create a new EC2 instance
instances = ec2.create_instances(
    # this uses my private azure hosted agent image
    ImageId='ami-04c8b6e7e894f20c1',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='key',
    Placement={
        #  change the AZ per your EBS AZ
        'AvailabilityZone': 'us-east-1a',
    },
    IamInstanceProfile={
        #  choose Arn or Name, not both
        'Arn': 'arn:aws:iam::account-id:instance-profile/azure-hosted-agent',
        # 'Name': 'hosted-agent'
    },

    SecurityGroupIds=[
        'sg-id',
    ],
    SubnetId='subnet-id',
    # if you have ebs you need to add that ebs subnet to mount
    # SubnetId='subnet-8be48dee',

    TagSpecifications=[
        {
            'ResourceType': 'instance',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'azure-linux-hosted-agent'
                },
                {
                    'Key': 'Function',
                    'Value': 'pipeline-linux-hosted-agent'
                },
            ]
        },
    ],

    InstanceMarketOptions={
        'MarketType': 'spot',
        'SpotOptions': {
            'MaxPrice': '1.000',
            'SpotInstanceType': 'one-time',
            'InstanceInterruptionBehavior': 'terminate'
        },
    }
)
