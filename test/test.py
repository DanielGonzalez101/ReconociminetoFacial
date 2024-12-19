# import boto3

# s3 = boto3.client('s3', region_name='us-east-1')
# try:
#     s3.list_buckets()
#     print("Conexión a S3 exitosa.")
# except Exception as e:
#     print(f"Error conectando a S3: {str(e)}")
import boto3
import uuid

s3 = boto3.client('s3', region_name='us-east-1')

S3_BUCKET = 'personas-imagenes'
img_filename = f"{uuid.uuid4()}.jpg"

# Generar una URL firmada
url = s3.generate_presigned_url('get_object',
                                Params={'Bucket': S3_BUCKET, 'Key': img_filename},
                                ExpiresIn=0)

print(url)