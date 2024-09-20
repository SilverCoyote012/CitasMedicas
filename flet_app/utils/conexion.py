import mysql.connector

def conexionDataBase():
    # Configuración de la conexión
    config = {
        'user': 'root',
        'password': '4er0p0st4lE_',
        'host': 'localhost',  # o la dirección IP de tu servidor MySQL
        'database': 'Clinica',
        'raise_on_warnings': True
    }

    conexion = mysql.connector.connect(**config)

    return conexion