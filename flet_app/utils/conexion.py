import mysql.connector

def conexionDataBase():
    # Configuración de la conexión
    config = {
        'user': 'root',
        'password': 'Alumno123',
        'host': 'localhost',  # o la dirección IP de tu servidor MySQL
        'database': 'Clinica',
        'raise_on_warnings': True
    }

    conexion = mysql.connector.connect(**config)

    return conexion