#This is code for starting and stopping ec2 instance during working day

import boto3
import datetime

ec2 = boto3.client('ec2', region_name='ap-south-1') 

def lambda_handler(event, context):
    
    current_day = datetime.datetime.today().weekday()
    
    
    if current_day < 5:
        
        ec2.start_instances(InstanceIds=['Instance_ID']) 
    else:
        
        ec2.stop_instances(InstanceIds=['Instance_id'])  

    return {
        'statusCode': 200,
        'body': 'EC2 instance state updated.'
    }
