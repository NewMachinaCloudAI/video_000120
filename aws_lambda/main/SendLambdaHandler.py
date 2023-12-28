import json
import boto3

def lambda_handler(event, context):
    
    # put message in SQS queue
    sqsMessageBody = {}
    sqsMessageBody['messageId'] = event['messageId']
    sqsMessageBody['messageDescription'] = event['messageDescription']
    sqsClient = boto3.client('sqs')
    message = sqsClient.send_message(
        QueueUrl='https://sqs.us-east-1.amazonaws.com/837868820500/video-000120-queue',
        MessageBody=json.dumps(sqsMessageBody)
    )

    return {
        'statusCode': 200,
        'body': json.dumps('Successful post to Amazon SQS queue')
    }