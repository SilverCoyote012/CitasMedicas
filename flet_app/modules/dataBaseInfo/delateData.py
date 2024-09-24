from utils.conexion import conexionDataBase

def eliminarDoctorDB(id_doctor):
    # Se elimina el doctor, el usuario y su domicilio de la base de datos
    # Sacar el id de usuario del doctor y el id de domicilio del doctor
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Usuario, ID_Direccion FROM Doctores WHERE ID_Doctor = %s"
    cursor.execute(consulta, (id_doctor,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    if resultado:
        id_usuario = resultado[0]
        id_direccion = resultado[1]

        # Eliminar el doctor
        conexion = conexionDataBase()
        cursor = conexion.cursor()
        consulta = "DELETE FROM Doctores WHERE ID_Doctor = %s"
        cursor.execute(consulta, (id_doctor,))
        conexion.commit()
        cursor.close()
        conexion.close()

        # Eliminar el usuario
        conexion = conexionDataBase()
        cursor = conexion.cursor()
        consulta = "DELETE FROM Usuarios WHERE ID_Usuario = %s"
        cursor.execute(consulta, (id_usuario,))
        conexion.commit()
        cursor.close()
        conexion.close()

        # Eliminar el domicilio
        conexion = conexionDataBase()
        cursor = conexion.cursor()
        consulta = "DELETE FROM Direcciones WHERE ID_Direccion = %s"
        cursor.execute(consulta, (id_direccion,))
        conexion.commit()
        cursor.close()
        conexion.close()