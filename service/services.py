import boto3
def aws_config():
    return boto3.session.Session(profile_name="demo")
def text_extract_client(aws_mang_config):
    return aws_mang_config.client(service_name='textract', region_name='us-east-1')
