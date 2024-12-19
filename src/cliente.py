import boto3
import uuid
from OB.ClienteOB import ClienteOB

# Configuración de AWS
dynamodb = boto3.resource('dynamodb', region_name='us-east-1')
s3 = boto3.client('s3', region_name='us-east-1')

DYNAMODB_TABLE = 'Users'
S3_BUCKET = 'persongonzalez'

def guardar_cliente(datos_formulario, archivo_img):
    """
    Procesa los datos del formulario, sube la imagen a S3 y guarda el cliente en DynamoDB.
    """
    # Extraer datos del formulario
    nombre = datos_formulario['nombre']
    apellido = datos_formulario['apellido']
    cedula = datos_formulario['cedula']
    edad = int(datos_formulario['edad'])
    imgDocumento = archivo_img

    # Crear objeto Cliente
    cliente = ClienteOB(nombre, apellido, cedula, edad, archivo_img)

    # Subir imagen a S3
    img_filename = f"{uuid.uuid4()}.jpg"
    s3.upload_fileobj(
        cliente.imgDocumento,
        S3_BUCKET,
        img_filename,
        ExtraArgs={'ContentType': archivo_img.content_type}
    )

    img_url = f"https://{S3_BUCKET}.s3.amazonaws.com/{img_filename}"
    # Guardar cliente en DynamoDB
    table = dynamodb.Table(DYNAMODB_TABLE)
    table.put_item(
        Item={
            'id': str(uuid.uuid4()),
            'cedula': cliente.cedula,
            'nombre': cliente.nombre,
            'apellido': cliente.apellido,
            'edad': cliente.edad,
            'imgDocumento': img_url
        }
    )
    print(f"Datos del formulario: {datos_formulario}")
    print(f"Archivo recibido: {archivo_img.filename}")
    print(f"Subiendo imagen a S3...")
    print(f"Guardando en DynamoDB...")


    return f"Cliente {cliente.nombre} guardado exitosamente."
