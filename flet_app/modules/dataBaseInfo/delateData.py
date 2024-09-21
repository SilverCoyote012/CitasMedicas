from utils.conexion import conexionDataBase

def eliminarDoctorDB(id_doctor):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Direccion, ID_Usuario FROM Doctores WHERE ID_Doctor = %s"
    cursor.execute(consulta, (id_doctor,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    id_direccion = resultado[0]
    id_usuario = resultado[1]

    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "DELETE FROM Doctores WHERE ID_Doctor = %s"
    cursor.execute(consulta, (id_doctor,))
    conexion.commit()
    cursor.close()
    conexion.close()

    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "DELETE FROM Domicilio_doctores WHERE ID_Domicilio = %s"
    cursor.execute(consulta, (id_direccion,))
    conexion.commit()
    cursor.close()
    conexion.close()

    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "DELETE FROM Usuarios WHERE ID_Usuario = %s"
    cursor.execute(consulta, (id_usuario,))
    conexion.commit()
    cursor.close()
    conexion.close()
