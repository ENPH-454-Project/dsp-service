import boto3
from scipy.io.wavfile import read, write

s3 = boto3.resource('s3')
client = boto3.client('s3')
bucket_name = "enph454-dsp-bucket"
filename = "you-need-to-grow-up.wav"

data = read("you-need-to-grow-up.wav")

#bucket = s3.Bucket('enph454-dsp-bucket')
#bucket.put_object(Key='test_wav', Body=data)
client.upload_file(filename,bucket_name,filename)

my_bucket = s3.Bucket(bucket_name)
for object in my_bucket.objects.all():
    print(object)
#for key in bucket:
#    print(key.key)