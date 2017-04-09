import pdb

import boto3

s3 = boto3.client('s3')

# call S3 to list current buckets
response = s3.list_buckets()

for bucket in response['Buckets']:
    print bucket['Name']

bucket_name = 'hello-world-youtube-video'

# bucket policy
bucket_policy = boto3.resource('s3').BucketPolicy(bucket_name)

response = bucket_policy.delete()

with open('./resources/bucket-policy.txt', 'r') as f:
    policy = f.read()

response = bucket_policy.put(Policy=policy)

pdb.set_trace()


# delete a bucket

s3.delete_bucket(Bucket=bucket_name)


# create a bucket
s3.create_bucket(Bucket=bucket_name)


# upload a file to the new bucket
# a managed uploader, which will split up large
# files automatically and upload parts in parallel.
filename = 'sometext.txt'
s3.upload_file('./resources/'+filename, bucket_name, filename)


