from utils.conexion import conexionDataBase

def agregarUsuarioDB(correo, password, rol):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Usuarios (Correo, Password, Rol) VALUES (%s, %s, %s)"
    cursor.execute(consulta, (correo, password, rol))
    conexion.commit()
    cursor.close()
    conexion.close()

    # Sacar el ID del usuario recien creado
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Usuario FROM Usuarios WHERE Correo = %s"
    cursor.execute(consulta, (correo,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    return resultado[0]

def agregarDoctorDB(nombre, apellido, telefono, especialidad, id_direccion, id_usuario):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Especialidad FROM Especialidades WHERE Especialidad = %s"
    cursor.execute(consulta, (especialidad,))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    id_especialidad = resultado[0]
    
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Doctores (Nombre, Apellido, Telefono, ID_Especialidad, ID_Direccion, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, apellido, telefono, id_especialidad, id_direccion, id_usuario))
    conexion.commit()
    cursor.close()
    conexion.close()

def agregarPacienteDB(nombre, apellido, fecha_nacimiento, sexo, telefono, id_direccion, id_usuario):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Pacientes (Nombre, Apellido, Fecha_Nacimiento, Sexo, Telefono, ID_Direccion, ID_Usuario) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (nombre, apellido, fecha_nacimiento, sexo, telefono, id_direccion, id_usuario))
    conexion.commit()
    cursor.close()
    conexion.close()

def agregarDomicilioDoctorDB(calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Domicilio_doctores (Calle, Numero_Domicilio, Codigo_Postal, Colonia, Ciudad, Estado, Pais) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais))
    conexion.commit()
    cursor.close()
    conexion.close()
    
    # Sacar el ID de la direccion recien creada
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Domicilio FROM Domicilio_doctores WHERE Calle = %s AND Numero_Domicilio = %s"
    cursor.execute(consulta, (calle, numero_domicilio))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    return resultado[0]

def agregarDomicilioPacienteDB(calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais):
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "INSERT INTO Domicilio_pacientes (Calle, Numero_Domicilio, Codigo_Postal, Colonia, Ciudad, Estado, Pais) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    cursor.execute(consulta, (calle, numero_domicilio, codigo_postal, colonia, ciudad, estado, pais))
    conexion.commit()
    cursor.close()
    conexion.close()

    # Sacar el ID de la direccion recien creada
    conexion = conexionDataBase()
    cursor = conexion.cursor()
    consulta = "SELECT ID_Direccion FROM Domicilio_pacientes WHERE Calle = %s AND Numero_Domicilio = %s"
    cursor.execute(consulta, (calle, numero_domicilio))
    resultado = cursor.fetchone()
    cursor.close()
    conexion.close()

    return resultado[0]