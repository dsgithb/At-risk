import boto3
import json
 
# WARNING: This is a bogus script for demonstration purposes only.
# Never include actual IAM access keys in your code.
 
# Fake IAM access key (DO NOT USE)
AWS_ACCESS_KEY_ID = 'AKIA4W4G6UB7YZSFZO6Q'
AWS_SECRET_ACCESS_KEY = 'Kqk2vJTxqCbOK7HFM+GdP9AR0fp2uU7SCbPru3tT'
 
def lambda_handler(event, context):
    # Initialize the S3 client with the fake credentials
    s3 = boto3.client('s3',
        aws_access_key_id=AWS_ACCESS_KEY_ID,
        aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
        region_name='us-west-2'
    )
    # List S3 buckets (this would fail with fake credentials)
    try:
        response = s3.list_buckets()
        buckets = [bucket['Name'] for bucket in response['Buckets']]
        return {
            'statusCode': 200,
            'body': json.dumps(f'S3 Buckets: {buckets}')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error: {str(e)}')
        }