import json
    
def lambda_handler(event, context):

    # Pull records from Event object
    records = event["Records"]
    
    # Display size of record array
    length = len( records )
    print ( "SQS Event: Number of Records = " + str(length) )

    # Loop through each record pulled from SQS queue
    for record in records:
        try:
            body = record["body"]
            message = json.loads(body)
    
            print("Message ID --> " + message["messageId"])
            print("Message Description -->" + message["messageDescription"])
            
        except Exception as innerException:
           print(innerException)
    
    return {
        'statusCode': 200,
        'body': json.dumps('Successful read of message from Amazon SQS')
    }