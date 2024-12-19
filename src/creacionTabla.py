import boto3

dynamodb = boto3.resource("dynamodb", region_name="us-east-1")


def crearTabla():
    #Ingresa el nombre de la tabla
    table_name = input("Ingresa el nombre de la tabla de los usuarios: ")#El nombre de la tabla de los usuarios es Usuarios

    existing_tables = boto3.client("dynamodb", region_name="us-east-1").list_tables()[
        "TableNames"
    ]

    if table_name not in existing_tables:
        table = dynamodb.create_table(
            TableName=table_name,
            KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],  # Llave primaria
            AttributeDefinitions=[
                {"AttributeName": "id", "AttributeType": "S"}  # 'S' significa String
            ],
            ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 5},
        )
        print(f"Creando la tabla {table_name}...")
        table.wait_until_exists()
        print("Tabla creada exitosamente.")
    else:
        print("La tabla ya esta creada")


crearTabla()