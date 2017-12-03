import boto3
import re
import os
from os import listdir
from os.path import isfile, join
from scipy.io.wavfile import read
bucket_name = 'enph454-dsp-bucket'
rec_path = 'C:/Users/Work/github/dsp-service/recordings'
cloud_sync_path = 'C:/Users/Work/github/dsp-service/cloud_folder'
def load_all_from_s3():
	s3 = boto3.resource('s3')
	for bucket in s3.buckets.all():
		for obj in bucket.objects.all():
			if obj.key.endswith('.wav'):
				file_path = os.path.join(cloud_sync_path, obj.key)
				s3.Object(obj.bucket_name, obj.key).download_file(file_path)
		
	
def save_to_s3():
	s3 = boto3.resource('s3')
	bucket = s3.Bucket(bucket_name)
	files = [f for f in listdir(rec_path) if isfile(join(rec_path, f))]
	for file in files:
		file_path = os.path.join(rec_path, file)
		data = read(file_path)
		s3.meta.client.upload_file(file_path,bucket_name,file)
	

save_to_s3()
load_all_from_s3()